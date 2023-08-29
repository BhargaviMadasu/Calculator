import tkinter as tk

def on_button_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 1, 4)  # Corrected button definition
]

for button_text, row, col, *span in buttons:
    rowspan = span[0] if span else 1
    columnspan = span[1] if len(span) > 1 else 1
    button = tk.Button(root, text=button_text, font=("Helvetica", 20), padx=20, pady=20)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
