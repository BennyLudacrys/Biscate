import smtplib
import ssl
from email.message import EmailMessage

from celery import Celery

from flaskauth.queue import queue
from flask import render_template
from flaskauth import app
from flask_mail import Mail, Message

# app = create_app()


mail = Mail(app)

# celery = Celery(app.name, broker='redis://localhost:6379/0')


def send_email(email_data):
    em = EmailMessage()
    em['From'] = app.config['MAIL_DEFAULT_SENDER']
    em['to'] = [email_data['to']]
    # msg = Message(email_data['subject'],
    #               sender=app.config['MAIL_DEFAULT_SENDER'],
    #               recipients=[email_data['to']])
    appName = app.config["APP_NAME"].capitalize()
    em.set_content(render_template(email_data['template']+'.txt', appName=appName, **email_data))
    # msg.html = render_template(email_data['template']+'.html', appName=appName, **email_data)
    # with app.app_context():
    #     mail.send(msg)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(app.config['MAIL_DEFAULT_SENDER'], 'evmlrpkyjigkisyq')  # Replace 'your_password' with your actual Gmail password
        smtp.sendmail(app.config['MAIL_DEFAULT_SENDER'], [email_data['to']], em.as_string())

