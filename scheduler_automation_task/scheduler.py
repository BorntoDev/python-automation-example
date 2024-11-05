import schedule
import time
from report_generator import generate_report
from email_sender import send_email

# กำหนดฟังก์ชันที่จะให้ทำงานตามเวลา
def daily_task():
    print("Running daily task...")
    report_file = generate_report()  # สร้างรายงาน
    send_email(report_file)          # ส่งรายงานทางอีเมล

# ตั้งเวลาให้ฟังก์ชันทำงานทุกวันตอน 8 โมงเช้า
schedule.every().day.at("08:00").do(daily_task)

# วนลูปเพื่อตรวจสอบตารางเวลาและรันงานเมื่อถึงเวลา
while True:
    schedule.run_pending()
    time.sleep(60)  # ตรวจสอบทุก ๆ 60 วินาที