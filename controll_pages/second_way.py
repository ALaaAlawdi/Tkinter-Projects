import tkinter as tk

def show_page(page_number):
    for page in pages:
        page.pack_forget()  # إخفاء جميع الصفحات

    pages[page_number].pack()  # إظهار الصفحة المطلوبة

root = tk.Tk()
root.title("صفحات متعددة")

# إنشاء الصفحات (Frames)
page1 = tk.Frame(root)
page2 = tk.Frame(root)
page3 = tk.Frame(root)

pages = [page1, page2, page3]  # قائمة لتخزين الصفحات

# محتوى الصفحة 1
label_page1 = tk.Label(page1, text="هذه هي الصفحة 1")
label_page1.pack()
button_goto_page2_from_1 = tk.Button(page1, text="انتقال إلى الصفحة 2", command=lambda: show_page(1))
button_goto_page2_from_1.pack()


# محتوى الصفحة 2
label_page2 = tk.Label(page2, text="هذه هي الصفحة 2")
label_page2.pack()
button_goto_page1_from_2 = tk.Button(page2, text="العودة إلى الصفحة 1", command=lambda: show_page(0))
button_goto_page1_from_2.pack()
button_goto_page3_from_2 = tk.Button(page2, text="انتقال إلى الصفحة 3", command=lambda: show_page(2))
button_goto_page3_from_2.pack()


# محتوى الصفحة 3
label_page3 = tk.Label(page3, text="هذه هي الصفحة 3")
label_page3.pack()
button_goto_page2_from_3 = tk.Button(page3, text="العودة إلى الصفحة 2", command=lambda: show_page(1))
button_goto_page2_from_3.pack()



# إظهار الصفحة الأولى عند بدء التشغيل
show_page(0)

root.mainloop()