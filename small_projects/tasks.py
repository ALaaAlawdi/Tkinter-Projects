import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)  # مسح مربع الإدخال
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال مهمة.")




def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("تحذير", "الرجاء تحديد مهمة لحذفها.")

def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        if "[مكتملة]" not in task:  # للتحقق من أن المهمة لم تُكمل من قبل
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, task + " [مكتملة]")
    except IndexError:
        messagebox.showwarning("تحذير", "الرجاء تحديد مهمة لإكمالها.")


root = tk.Tk()
root.title("مدير المهام البسيط")

# إضافة مهمة
label_task = tk.Label(root, text="المهمة:")
label_task.grid(row=0, column=0, padx=5, pady=5)

entry_task = tk.Entry(root)
entry_task.grid(row=0, column=1, padx=5, pady=5)

button_add_task = tk.Button(root, text="إضافة مهمة", command=add_task)
button_add_task.grid(row=1, column=0, columnspan=2, pady=5)

# قائمة المهام
listbox_tasks = tk.Listbox(root)
listbox_tasks.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# أزرار التحكم
button_delete_task = tk.Button(root, text="حذف مهمة", command=delete_task)
button_delete_task.grid(row=3, column=0, padx=5, pady=5)
button_complete_task = tk.Button(root, text="إكمال مهمة", command=complete_task)
button_complete_task.grid(row=3, column=1, padx=5, pady=5)


root.mainloop()