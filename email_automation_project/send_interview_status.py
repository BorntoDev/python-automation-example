import smtplib
from email.message import EmailMessage
import pandas as pd
from dotenv import load_dotenv
import os

# โหลดข้อมูลจากไฟล์ .env
load_dotenv()

# ข้อมูลการเข้าสู่ระบบอีเมลจาก .env
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# ดึงข้อมูลผู้รับจากไฟล์ CSV
recipients_data = pd.read_csv("C:\\Users\\User\\Content\\7-use-case-python-automation\\email_automation_project\\data\\recipients.csv")  # ไฟล์ CSV ที่มีคอลัมน์ 'name', 'email', 'status'

# เทมเพลตข้อความอีเมล
email_template = """
สวัสดีคุณ {name},

เราขอแจ้งสถานะการสัมภาษณ์งานของคุณ:
{status}

ขอบคุณที่ให้ความสนใจในโอกาสนี้ และหากมีข้อสงสัยเพิ่มเติม กรุณาติดต่อเราได้ที่ทีมฝ่ายบุคคล
ขอแสดงความนับถือ,
ทีมงาน
"""

# ฟังก์ชันส่งอีเมล
def send_email(recipient_name, recipient_email, status):
    msg = EmailMessage()
    msg['Subject'] = "สถานะการสัมภาษณ์งานของคุณ"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email

    # ใส่ข้อมูลลงในเทมเพลต
    msg.set_content(email_template.format(name=recipient_name, status=status))

    # ส่งอีเมล
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"Email sent to {recipient_name} ({recipient_email})")

# ส่งอีเมลให้ผู้รับทุกคนในไฟล์ CSV
for index, row in recipients_data.iterrows():
    send_email(row['name'], row['email'], row['status'])
