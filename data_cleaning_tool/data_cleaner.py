import pandas as pd

# อ่านข้อมูลจากไฟล์ CSV ต้นฉบับ
input_file = "data/raw_data.csv"
output_file = "data/cleaned_data.csv"

def clean_data(input_file, output_file):
    # อ่านไฟล์ CSV
    df = pd.read_csv(input_file)
    
    # ตรวจสอบว่าคอลัมน์ 'Name' และ 'Income' มีอยู่ก่อนดำเนินการลบค่า NaN
    required_columns = ["Name", "Income"]
    available_columns = [col for col in required_columns if col in df.columns]
    
    # ลบแถวที่มีค่า NaN ในคอลัมน์ที่สำคัญ
    if available_columns:
        df.dropna(subset=available_columns, inplace=True)
    
    # เติมค่า NaN ในคอลัมน์ 'Age' ด้วยค่าเฉลี่ยของอายุ (ถ้าคอลัมน์ 'Age' มีอยู่)
    if "Age" in df.columns:
        df['Age'].fillna(df['Age'].mean(), inplace=True)
    
    # กำจัดข้อมูลที่ซ้ำซ้อน (Duplicates) ตามคอลัมน์ทั้งหมด
    df.drop_duplicates(inplace=True)
    
    # แปลงประเภทข้อมูล (Data Type) ของคอลัมน์ 'Income' เป็นตัวเลข (ถ้าคอลัมน์ 'Income' มีอยู่)
    if "Income" in df.columns:
        df["Income"] = pd.to_numeric(df["Income"], errors='coerce')
    
    # บันทึกข้อมูลที่ถูกทำความสะอาดแล้วลงในไฟล์ CSV ใหม่
    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")

# เรียกใช้ฟังก์ชันทำความสะอาดข้อมูล
clean_data(input_file, output_file)