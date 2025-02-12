import tkinter as tk
import sqlite3

def save_data():
    name = entry_name.get()
    age = entry_age.get()

    if name and age:
        try:
            conn = sqlite3.connect('data.db')  # إنشاء/الاتصال بقاعدة البيانات
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
            conn.commit()
            conn.close()
            print("تم حفظ البيانات.")
        except Exception as e:
            print("حدث خطأ:", e)
    else:
        print("الرجاء إدخال الاسم والعمر.")

root = tk.Tk()
root.title("تطبيق قاعدة بيانات")

label_name = tk.Label(root, text="الاسم:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_age = tk.Label(root, text="العمر:")
label_age.grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

button_save = tk.Button(root, text="حفظ", command=save_data)
button_save.grid(row=2, column=0, columnspan=2)

# إنشاء جدول المستخدمين إذا لم يكن موجودًا
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")
conn.commit()
conn.close()


root.mainloop()

