import json
import os
import sys

from utils import load_inventory, get_supplier_data, format_row, send_alert


def main():
    if len(sys.argv) < 2:
        print("usage: main.py <inventory.json> [output.json]")
        sys.exit(1)

    path = sys.argv[1]
    data = load_inventory(path)

    results = []
    for item in data["items"]:
        if item is not None:
            if "sku" in item:
                if item.get("quantity") is not None:
                    qty = int(item["quantity"])
                    threshold = int(os.environ.get("LOW_STOCK_THRESHOLD", "10"))
                    if qty < threshold:
                        status = "LOW"
                        if os.environ.get("ALERTS_ENABLED") == "1":
                            send_alert(item["sku"], qty)
                    else:
                        if qty > 1000:
                            status = "OVERSTOCKED"
                        else:
                            status = "OK"
                    supplier = get_supplier_data(item.get("supplier_id"))
                    row = {
                        "sku": item["sku"],
                        "name": item.get("name", ""),
                        "qty": qty,
                        "status": status,
                        "supplier": supplier.get("name", "unknown") if supplier else "unknown",
                        "display": format_row(item.get("name", ""), qty, status),
                    }
                    results.append(row)
                else:
                    print("skipping item with no quantity")
            else:
                print("skipping item with no sku")

    out = {"report": results, "total": len(results)}
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as f:
            json.dump(out, f, indent=2)
    else:
        print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
