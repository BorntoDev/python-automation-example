import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(report_path):
    # ข้อมูลเซิร์ฟเวอร์อีเมลและผู้ส่ง
    sender_email = "sender_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "รหัสผ่านของ Gmail หรือ App Password หากใช้การยืนยันสองขั้นตอน"  
    subject = "Daily Sales Report"
    body = "Please find the attached daily sales report."

    # สร้างอีเมล
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # แนบไฟล์รายงาน
    with open(report_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=os.path.basename(report_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
        msg.attach(part)

    # ตั้งค่าการเชื่อมต่อและส่งอีเมลผ่าน Gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully.")
