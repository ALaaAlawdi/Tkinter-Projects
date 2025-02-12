import tkinter as tk
from tkinter import ttk  # لتحسين المظهر
import requests
import json

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        url = f"https://api.exchangeratesapi.io/latest?base={from_currency}" # رابط API
        response = requests.get(url)
        data = response.json()

        if "rates" in data and to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            converted_amount = amount * rate
            result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}") # تنسيق الناتج لرقمين عشريين
        else:
             result_label.config(text="خطأ: عملة غير مدعومة")

    except ValueError:
        result_label.config(text="خطأ في الإدخال")
    except requests.exceptions.RequestException:
        result_label.config(text="خطأ في الاتصال بالإنترنت")
    except (KeyError, TypeError): # للتعامل مع أخطاء البيانات من API
         result_label.config(text="خطأ في جلب سعر الصرف")


root = tk.Tk()
root.title("محول العملات")

# عناصر واجهة المستخدم
amount_label = ttk.Label(root, text="المبلغ:")
amount_label.grid(row=0, column=0, padx=5, pady=5)

entry_amount = ttk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

from_currency_label = ttk.Label(root, text="من عملة:")
from_currency_label.grid(row=1, column=0, padx=5, pady=5)

from_currency_var = tk.StringVar(value="USD")  # القيمة الافتراضية
from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=["USD", "EUR", "GBP", "JPY", "SAR"]) # يمكنك إضافة المزيد من العملات
from_currency_menu.grid(row=1, column=1, padx=5, pady=5)

to_currency_label = ttk.Label(root, text="إلى عملة:")
to_currency_label.grid(row=2, column=0, padx=5, pady=5)

to_currency_var = tk.StringVar(value="SAR")  # القيمة الافتراضية
to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=["USD", "EUR", "GBP", "JPY", "SAR"]) # نفس العملات
to_currency_menu.grid(row=2, column=1, padx=5, pady=5)

convert_button = ttk.Button(root, text="تحويل", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)


root.mainloop()