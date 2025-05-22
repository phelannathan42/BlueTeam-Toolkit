import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@example.com"
    msg["To"] = "admin@example.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.send_message(msg)

send_alert("Suspicious Login Attempt", "Multiple failed login attempts detected in NGINX logs.")
