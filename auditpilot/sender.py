"""Send drafted emails through YOUR mailbox, slowly, with a hard daily cap."""
import os
import smtplib
import ssl
import time
from email.message import EmailMessage


def build(lead, cfg):
    msg = EmailMessage()
    msg["From"] = f'{cfg["your_name"]} <{cfg["reply_email"]}>'
    msg["To"] = lead["email"]
    msg["Subject"] = lead["subject"]
    msg["Reply-To"] = cfg["reply_email"]
    msg.set_content(lead["body"])
    return msg


def connect(cfg):
    smtp = cfg["smtp"]
    password = os.environ.get(smtp.get("password_env", "AUDITPILOT_SMTP_PASSWORD"))
    if not password:
        raise SystemExit(f'Set the {smtp.get("password_env")} environment variable to your SMTP password '
                         "(never put the password in config.json).")
    server = smtplib.SMTP(smtp["host"], smtp.get("port", 587), timeout=30)
    server.starttls(context=ssl.create_default_context())
    server.login(smtp["username"], password)
    return server


def send_batch(leads, cfg, on_sent, pause=None, server=None):
    """Send each lead's draft; calls on_sent(lead) after each success. Returns count sent."""
    pause = cfg.get("seconds_between_sends", 45) if pause is None else pause
    own = server is None
    server = server or connect(cfg)
    sent = 0
    try:
        for n, lead in enumerate(leads):
            if n and pause:
                time.sleep(pause)
            server.send_message(build(lead, cfg))
            on_sent(lead)
            sent += 1
    finally:
        if own:
            server.quit()
    return sent
