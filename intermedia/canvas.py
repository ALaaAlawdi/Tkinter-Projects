import tkinter as tk
from PIL import Image, ImageTk  #  PIL (Pillow) للتعامل مع الصور

root = tk.Tk()
root.title("نافذتي مع صورة")

# فتح الصورة وتحويلها إلى صيغة Tkinter
try:
    image = Image.open("profile.jpg")  #  ضع مسار صورتك هنا
    photo = ImageTk.PhotoImage(image)

    # عرض الصورة في Label
    label = tk.Label(root, image=photo)
    label.image = photo  #  هام: يجب الاحتفاظ بمرجع للصورة لمنع حذفها من الذاكرة
    label.pack()

except FileNotFoundError:
    print("الصورة غير موجودة!")


root.mainloop()