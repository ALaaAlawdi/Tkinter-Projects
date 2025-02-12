import tkinter as tk

root = tk.Tk()
root.title("نافذتي مع قائمة")

# إنشاء قائمة
listbox = tk.Listbox(root, selectmode=tk.SINGLE)  #  MULTIPLE يسمح باختيار عدة عناصر

# إضافة عناصر إلى القائمة
listbox.insert(tk.END, "العنصر الأول")
listbox.insert(tk.END, "العنصر الثاني")
listbox.insert(tk.END, "العنصر الثالث")
listbox.insert(tk.END, "العنصر الرابع")

listbox.pack()

def show_selected():
    selected_indices = listbox.curselection()  # الحصول على أرقام العناصر المختارة
    selected_items = [listbox.get(index) for index in selected_indices] # الحصول على النصوص المختارة
    print("العناصر المختارة:", selected_items)

button = tk.Button(root, text="إظهار العناصر المختارة", command=show_selected)
button.pack()


root.mainloop()