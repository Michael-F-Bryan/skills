import json
import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils


def test_get_supplier_data_calls_api():
    with mock.patch("utils.urllib.request.urlopen") as m:
        m.return_value.__enter__.return_value.read.return_value = json.dumps(
            {"name": "Acme"}
        ).encode()
        result = utils.get_supplier_data("s1")
        m.assert_called_once()
        assert result["name"] == "Acme"


def test_send_alert_posts_webhook(monkeypatch):
    monkeypatch.setenv("ALERT_WEBHOOK_URL", "https://hooks.example.com/x")
    with mock.patch("utils.urllib.request.urlopen") as m:
        utils.send_alert("SKU-1", 3)
        m.assert_called_once()


def test_format_row():
    out = utils.format_row("Widget", 5, "LOW")
    assert "Widget" in out
