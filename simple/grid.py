import tkinter as tk

root = tk.Tk()
root.title("نافذتي مع Grid")

# عناصر
label_name = tk.Label(root, text="الاسم:")
entry_name = tk.Entry(root)
label_age = tk.Label(root, text="العمر:")
entry_age = tk.Entry(root)
button_submit = tk.Button(root, text="إرسال" )

# استخدام grid
label_name.grid(row=0, column=0, padx=5, pady=5)  # الصف 0، العمود 0
entry_name.grid(row=0, column=1, padx=5, pady=5)  # الصف 0، العمود 1
label_age.grid(row=1, column=0, padx=5, pady=5)  # الصف 1، العمود 0
entry_age.grid(row=1, column=1, padx=5, pady=5)  # الصف 1، العمود 1

button_submit.grid(row=2, column=0, columnspan=2, pady=10) # الصف 2، يمتد على عمودين

root.mainloop()