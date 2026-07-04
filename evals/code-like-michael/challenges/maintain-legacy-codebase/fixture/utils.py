import json
import os
import urllib.request


def load_inventory(path):
    with open(path) as f:
        data = json.load(f)
    return data


def get_supplier_data(supplier_id):
    if supplier_id is None:
        return None
    base = os.environ.get("SUPPLIER_API_URL", "https://suppliers.internal.example.com")
    try:
        with urllib.request.urlopen(f"{base}/suppliers/{supplier_id}", timeout=5) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def format_row(name, qty, status):
    return "%-30s %5d  %s" % (name[:30], qty, status)


def send_alert(sku, qty):
    webhook = os.environ.get("ALERT_WEBHOOK_URL")
    if not webhook:
        return
    payload = json.dumps({"text": f"Low stock: {sku} ({qty} left)"}).encode()
    req = urllib.request.Request(webhook, data=payload, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass


def chunk_list(lst, n):
    # currently unused but might be handy later
    return [lst[i : i + n] for i in range(0, len(lst), n)]
