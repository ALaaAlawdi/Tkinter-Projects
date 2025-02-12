import tkinter as tk

root = tk.Tk()
root.title("نافذتي مع Place")

# عناصر
label_name = tk.Label(root, text="الاسم:")
entry_name = tk.Entry(root)
button_submit = tk.Button(root, text="إرسال")

# استخدام place
label_name.place(x=10, y=10)
entry_name.place(x=80, y=10)
button_submit.place(x=50, y=50)

root.mainloop()