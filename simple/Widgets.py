import tkinter as tk


def add_widgets():
    print("تم تشغيل الدالة")

    
root = tk.Tk()
root.title("نافذتي مع عناصر")

# زر
button = tk.Button(root, text="اضغطني", command= lambda :add_widgets() )  #  lambda تستخدم لتعريف دالة صغيرة
button.pack() #  تحديد مكان الزر في النافذة (هناك طرق أخرى مثل grid و place)

# نص ثابت (Label)
label = tk.Label(root, text="هذا نص")
label.pack()

# مربع إدخال النص (Entry)
entry = tk.Entry(root)
entry.pack()

root.mainloop()

