import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, result)
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

screen = tk.Entry(root, font="Helvetica 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+'
]

row = 0
col = 0
for button in buttons:
    b = tk.Button(button_frame, text=button, font="Helvetica 15 bold", relief=tk.GROOVE, border=0)
    b.grid(row=row, column=col, ipadx=10, ipady=10, padx=10, pady=10)
    b.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()
