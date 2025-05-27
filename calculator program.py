from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.set(result)
        except Exception as e:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

# GUI setup
root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = StringVar()
entry.set("")

entry_field = Entry(root, textvar=entry, font="Arial 20", justify=RIGHT, bd=10, relief=SUNKEN)
entry_field.pack(fill=X, ipadx=8, ipady=15, pady=10, padx=10)

# Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = Frame(root)
    frame.pack()
    for btn in row:
        button = Button(frame, text=btn, font="Arial 18", width=5, height=2)
        button.pack(side=LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()