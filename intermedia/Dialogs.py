import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("نافذتي مع نوافذ فرعية")

def show_message():
    messagebox.showinfo("رسالة", "هذه رسالة معلومات.")

def ask_question():
    result = messagebox.askyesno("سؤال", "هل أنت متأكد؟")  #  askyesno  تُرجع  True  أو  False
    if result:
        print("أجاب بنعم.")
    else:
        print("أجاب بلا.")

def get_input():
    name = simpledialog.askstring("إدخال", "أدخل اسمك:")  #  askstring  تُرجع النص الذي أدخله المستخدم
    if name:
        print("الاسم المدخل:", name)

button_message = tk.Button(root, text="إظهار رسالة", command=show_message)
button_message.pack()

button_question = tk.Button(root, text="طرح سؤال", command=ask_question)
button_question.pack()

button_input = tk.Button(root, text="الحصول على إدخال", command=get_input)
button_input.pack()


root.mainloop()