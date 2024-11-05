import pyautogui
import time

# รอเวลาให้เราเปิดหน้าเว็บก่อนที่จะเริ่มกรอกข้อมูล
time.sleep(10)

# กรอกชื่อเต็ม (Full Name)
pyautogui.click(x=453, y=603)  # กำหนดตำแหน่ง x, y ของฟิลด์ Full Name
pyautogui.write("Sirasit Boonklang", interval=0.1)

# กรอกระดับความสามารถในการรับมือแรงกดดัน (Pressure Handling)
pyautogui.click(x=453, y=770)  # กำหนดตำแหน่ง x, y ของฟิลด์ Pressure
pyautogui.write("90", interval=0.1)

# เลือกระดับความสามารถในการสื่อสารกับแฟนบอล (Fan Interaction Level)
pyautogui.click(x=453, y=938)  # กำหนดตำแหน่ง x, y ของ Dropdown Fan Interaction
pyautogui.press("down", presses=1)  # เลือก "Good" (สามารถเปลี่ยนจำนวนการกดได้)
pyautogui.press("enter")

# กรอกระดับความโกรธต่อการทำงานของคู่แข่ง (Rival Anger Level)
pyautogui.click(x=453, y=1111)  # กำหนดตำแหน่ง x, y ของฟิลด์ Rival Anger Level
pyautogui.write("7", interval=0.1)

# ติ๊กเลือก "พร้อมรับคำวิจารณ์จากแฟนบอลและสื่อ" (Handle Criticism)
pyautogui.click(x=434, y=1196)  # กำหนดตำแหน่ง x, y ของ Checkbox Handle Criticism

# คลิกปุ่ม "ส่งใบสมัคร"
pyautogui.click(x=666, y=1265)  # กำหนดตำแหน่ง x, y ของปุ่ม Submit

print("Form submitted automatically!")
