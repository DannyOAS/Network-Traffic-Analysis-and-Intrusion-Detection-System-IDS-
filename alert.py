import smtplib

def send_email_alert(ip):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        sender_email = "youremail@gmail.com"
        sender_password = "yourpassword"
        recipient_email = "recipientemail@gmail.com"

        server.login(sender_email, sender_password)
        subject = "Intrusion Alert"
        body = f"Suspicious activity detected from IP: {ip}. Possible SYN Flood attack."
        message = f'Subject: {subject}\n\n{body}'

        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        print(f"Alert email sent for suspicious IP: {ip}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
