import tkinter as tk
from tkinter import messagebox

class MyApplication:
    def __init__(self, master):
        self.master = master
        master.title("تطبيقي")

        # عناصر الواجهة
        self.label = tk.Label(master, text="أدخل اسمك:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.button = tk.Button(master, text="إرسال", command=self.greet)
        self.button.grid(row=1, column=0, columnspan=2, pady=10)

    def greet(self):
        name = self.entry.get()
        if name:
            messagebox.showinfo("تحية", f"مرحباً، {name}!")
        else:
            messagebox.showerror("خطأ", "الرجاء إدخال اسمك.")


root = tk.Tk()
app = MyApplication(root)  # إنشاء كائن من الكلاس
root.mainloop()