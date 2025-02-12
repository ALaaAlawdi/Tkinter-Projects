import tkinter as tk
from tkinter import ttk  # استيراد ttk

root = tk.Tk()
root.title("واجهة مستخدم جذابة")

# استخدام ttk لتحسين المظهر
style = ttk.Style()
style.theme_use("clam")  # اختيار مظهر (يمكنك تجربة مظاهر أخرى)

label = ttk.Label(root, text="هذا نص جميل", font=("Arial", 16), foreground="blue")
label.pack(pady=10)

button = ttk.Button(root, text="اضغطني", style="My.TButton")  # استخدام ستايل مخصص
button.pack(pady=5)

# تعريف ستايل مخصص للزر
style.configure("My.TButton", font=("Verdana", 12), foreground="green", padding=6)

root.mainloop()