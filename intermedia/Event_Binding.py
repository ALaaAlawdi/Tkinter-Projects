import tkinter as tk

root = tk.Tk()
root.title("نافذتي مع ربط الأحداث")

def on_click(event):
    print("تم الضغط على الزر عند:", event.x, event.y)  #  event.x و event.y  يُرجعان إحداثيات  الضغط

button = tk.Button(root, text="اضغطني")
button.bind("<Button-1>", on_click)  #  ربط حدث الضغط بزر الفأرة الأيسر (Button-1) بالدالة on_click
button.pack()

entry = tk.Entry(root)
entry.pack()

def on_key_press(event):
    print("تم ضغط مفتاح:", event.char)  # event.char  يُرجع الحرف الذي تم ضغطه

entry.bind("<Key>", on_key_press)  # ربط حدث ضغط أي مفتاح بالدالة on_key_press

root.mainloop()