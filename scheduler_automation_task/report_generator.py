import pandas as pd
from fpdf import FPDF

def generate_report():
    # สร้าง DataFrame ตัวอย่าง
    data = {
        "Month": ["January", "February", "March"],
        "Sales": [1500, 1700, 1800]
    }
    df = pd.DataFrame(data)

    # สร้างรายงาน PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Monthly Sales Report", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    for i, row in df.iterrows():
        pdf.cell(200, 10, f"{row['Month']}: ${row['Sales']}", ln=True)

    # บันทึกรายงาน PDF
    report_path = "daily_sales_report.pdf"
    pdf.output(report_path)
    print("Report generated:", report_path)
    return report_path  # คืนค่า path ของรายงาน
