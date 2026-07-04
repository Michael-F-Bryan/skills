"""Tests for utils — some are weak."""

from utils import build_user_record, validate_email


def test_validate_email_accepts_at_sign():
    assert validate_email("a@b.com")


def test_build_user_record():
    rec = build_user_record({"email": "a@b.com", "first_name": "Ada", "last_name": "Lovelace"})
    assert rec is not None
    assert rec["email"] == "a@b.com"
