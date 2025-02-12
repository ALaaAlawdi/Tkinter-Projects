import tkinter as tk

root = tk.Tk()
root.title("نافذتي مع حدث")

entry = tk.Entry(root)
entry.pack()

def show_text():
    text = entry.get()  #  الحصول على النص من مربع الإدخال
    print("النص المدخل:", text)

button = tk.Button(root, text="إظهار النص", command=show_text)
button.pack()

root.mainloop()