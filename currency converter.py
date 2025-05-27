from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import messagebox

# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get().upper()
        to_curr = to_currency.get().upper()

        converter = CurrencyRates()
        result = converter.convert(from_curr, to_curr, amount)
        result_label.config(text=f"{amount} {from_curr} = {round(result, 2)} {to_curr}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input or currency code")

# GUI Setup
root = Tk()
root.title("Currency Converter")
root.geometry("400x300")

Label(root, text="Currency Converter", font=("Arial", 18)).pack(pady=10)

Label(root, text="Amount").pack()
amount_entry = Entry(root)
amount_entry.pack(pady=5)

Label(root, text="From Currency (e.g. USD)").pack()
from_currency = Entry(root)
from_currency.pack(pady=5)

Label(root, text="To Currency (e.g. INR)").pack()
to_currency = Entry(root)
to_currency.pack(pady=5)

Button(root, text="Convert", command=convert_currency, font=("Arial", 12)).pack(pady=15)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
