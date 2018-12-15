from threading import Thread
from flask import current_app
from flask_mail import Message
from twilio.rest import Client


def send_async_email(app, msg):
    with app.app_context():
        from app import mail
        mail.send(msg)


def send_email(to, subject, body):
    app = current_app._get_current_object()
    msg = Message(subject=subject,
                  sender=app.config.get('MAIL_USERNAME'),
                  recipients=[to],
                  reply_to=app.config.get("MAIL_USERNAME"),
                  body=body)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def send_sms(to,body):
    account_sid = current_app.config.get("ACCOUNT_SID")
    auth_token = current_app.config.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=current_app.config.get("DEFAULT_PHONE_NUMBER"),
        body=body,
        to=to
    )
    return None
