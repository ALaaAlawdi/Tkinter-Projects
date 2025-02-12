import tkinter as tk

root = tk.Tk()
root.title("نافذتي مع شريط تمرير")

# إنشاء شريط تمرير
scrollbar = tk.Scrollbar(root)

# إنشاء قائمة وربطها بشريط التمرير
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set) # yscrollcommand يربط القائمة بشريط التمرير

# إضافة عناصر كثيرة إلى القائمة (لإظهار الحاجة إلى شريط التمرير)
for i in range(50):
    listbox.insert(tk.END, f"العنصر {i+1}")

# وضع شريط التمرير والقائمة في النافذة
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)  #  side=RIGHT يضع الشريط على اليمين، fill=Y يجعله يمتد عمودياً
listbox.pack(side=tk.LEFT, fill=tk.BOTH)   # side=LEFT يضع القائمة على اليسار، fill=BOTH يملأ المساحة المتاحة

# ربط شريط التمرير بالقائمة
scrollbar.config(command=listbox.yview)  # يربط حركة شريط التمرير بتحريك القائمة

root.mainloop()