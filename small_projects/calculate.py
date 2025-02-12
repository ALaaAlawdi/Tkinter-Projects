import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "لا يمكن القسمة على الصفر"
            else:
                result = num1 / num2
        else:
            result = "Invalid Operator"

        result_label.config(text="النتيجة: " + str(result))

    except ValueError:
        result_label.config(text="خطأ في الإدخال")



root = tk.Tk()
root.title("آلة حاسبة بسيطة")

# الإدخال الأول
label_num1 = tk.Label(root, text="الرقم الأول:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# الإدخال الثاني
label_num2 = tk.Label(root, text="الرقم الثاني:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# اختيار العملية
operator_var = tk.StringVar(value="+")  # القيمة الافتراضية هي الجمع
operator_label = tk.Label(root, text="العملية:")
operator_label.grid(row=2, column=0, padx=5, pady=5)
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=2, column=1, padx=5, pady=5)

# زر الحساب
calculate_button = tk.Button(root, text="احسب", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# عرض النتيجة
result_label = tk.Label(root, text="النتيجة:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()