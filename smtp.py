import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from line_notify import line_notify

load_dotenv()


def send_mail(subject, message):
    # 環境変数からSMTPサーバーの情報を取得
    smtp_server = os.getenv('SMTP_SERVER')
    from_email = os.getenv('from_email')
    user_id = os.getenv('USER_ID')
    password = os.getenv('MAIL_PASSWORD')
    smtp_port = 587
    to_email = os.getenv('TO_EMAIL')

    # メールの組み立て
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # SMTPサーバーに接続し、メールを送信
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user_id, password)
        server.sendmail(from_email, to_email, msg.as_string())
    except (smtplib.SMTPException, smtplib.SMTPAuthenticationError) as e:
        line_notify(f'メール送信に失敗しました: {e}')
    finally:
        server.quit()


if __name__ == '__main__':
    send_mail('テストメール', 'テストメールです。')
