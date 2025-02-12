import tkinter as tk

def open_page2():
    root.withdraw()  # إخفاء النافذة الرئيسية
    page2 = tk.Toplevel(root)  # إنشاء نافذة جديدة (صفحة 2)
    page2.title("الصفحة 2")

    label_page2 = tk.Label(page2, text="هذه هي الصفحة 2")
    label_page2.pack()

    back_button = tk.Button(page2, text="العودة إلى الصفحة الرئيسية", command=lambda: [page2.destroy(), root.deiconify()]) # دالة lambda لإرجاع الصفحة الرئيسية
    back_button.pack()



root = tk.Tk()
root.title("الصفحة الرئيسية")

label_page1 = tk.Label(root, text="هذه هي الصفحة الرئيسية")
label_page1.pack()

button_open_page2 = tk.Button(root, text="انتقال إلى الصفحة 2", command=open_page2)
button_open_page2.pack()



root.mainloop()