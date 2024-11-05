from bs4 import BeautifulSoup
import pandas as pd
import os

# ระบุ path ของไฟล์ HTML ที่ต้องการดึงข้อมูล
file_path = "path ของไฟล์ HTML"

# เปิดไฟล์ HTML และอ่านข้อมูล
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# แปลง HTML ที่ได้มาเป็น BeautifulSoup object
soup = BeautifulSoup(content, 'html.parser')

# สร้างลิสต์สำหรับเก็บข้อมูลที่ดึงมา
data = []

# ค้นหาข้อมูลที่ต้องการจาก HTML (ตัวอย่าง: ดึงชื่อและราคา)
products = soup.find_all('div', class_='product')  # ปรับ class ตามเว็บไซต์จริง
for product in products:
    name = product.find('h2').text.strip()  # ดึงชื่อสินค้า
    price = product.find('span', class_='price').text.strip()  # ดึงราคาสินค้า
    data.append({'Name': name, 'Price': price})

# สร้าง DataFrame จากลิสต์ข้อมูล
df = pd.DataFrame(data)

# ตรวจสอบว่ามีโฟลเดอร์ output หรือไม่ ถ้าไม่มีให้สร้างใหม่
if not os.path.exists("output"):
    os.makedirs("output")

# บันทึกข้อมูลในรูปแบบ CSV
df.to_csv("output/products_data.csv", index=False)
print("Data has been saved to output/products_data.csv")
