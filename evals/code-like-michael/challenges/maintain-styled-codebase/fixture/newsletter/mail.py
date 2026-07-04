from __future__ import annotations

import smtplib
from collections.abc import Callable
from email.message import EmailMessage

from newsletter.types import MailConfig, MailDeliveryError, StoredArticle

SmtpSender = Callable[[MailConfig, EmailMessage], None]


def default_smtp_sender(mail: MailConfig, message: EmailMessage) -> None:
    try:
        with smtplib.SMTP(mail.smtp_host, mail.smtp_port, timeout=30) as smtp:
            if mail.use_tls:
                smtp.starttls()
            if mail.username:
                smtp.login(mail.username, mail.password)
            smtp.send_message(message)
    except smtplib.SMTPException as exc:
        recipient = mail.to_addrs[0] if mail.to_addrs else "(unknown)"
        raise MailDeliveryError(recipient, str(exc)) from exc


def build_digest_body(articles: list[StoredArticle]) -> str:
    if not articles:
        return "No new articles met the relevance threshold."

    lines = ["Newsletter digest", ""]
    for article in articles:
        lines.append(f"[{article.score:.2f}] {article.title}")
        lines.append(f"  feed: {article.feed_name}")
        if article.link:
            lines.append(f"  link: {article.link}")
        if article.summary:
            snippet = article.summary.replace("\n", " ")
            lines.append(f"  {snippet[:240]}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def send_digest(
    mail: MailConfig,
    articles: list[StoredArticle],
    *,
    sender: SmtpSender = default_smtp_sender,
) -> None:
    message = EmailMessage()
    message["Subject"] = f"Newsletter digest ({len(articles)} articles)"
    message["From"] = mail.from_addr
    message["To"] = ", ".join(mail.to_addrs)
    message.set_content(build_digest_body(articles))
    sender(mail, message)
