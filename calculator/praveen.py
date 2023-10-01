from tkinter import *

root = Tk()
root.title("Calculator")

# Entry widget for input
input = Entry(root, width=25, font=("Helvetica", 20))
input.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Button click handler
def click(num):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(num))

# Math operation functions
def add():
    current = input.get()
    global fnum
    fnum = float(current)
    global math_op
    math_op = "add"
    input.delete(0, END)

def subtract():
    current = input.get()
    global fnum
    fnum = float(current)
    global math_op
    math_op = "subtract"
    input.delete(0, END)

def multiply():
    current = input.get()
    global fnum
    fnum = float(current)
    global math_op
    math_op = "multiply"
    input.delete(0, END)

def divide():
    current = input.get()
    global fnum
    fnum = float(current)
    global math_op
    math_op = "divide"
    input.delete(0, END)

# Clear and equals functions
def clear():
    input.delete(0, END)

def equal():
    current = input.get()
    snum = float(current)
    input.delete(0, END)
    if math_op == "add":
        input.insert(0, str(fnum + snum))
    elif math_op == "subtract":
        input.insert(0, str(fnum - snum))
    elif math_op == "multiply":
        input.insert(0, str(fnum * snum))
    elif math_op == "divide":
        if snum != 0:
            input.insert(0, str(fnum / snum))
        else:
            input.insert(0, "Error")

# Create buttons with styles
button_style = {
    "padx": 20,
    "pady": 20,
    "font": ("Helvetica", 16),
}

button_1 = Button(root, text="1", command=lambda: click(1), **button_style)
button_2 = Button(root, text="2", command=lambda: click(2), **button_style)
button_3 = Button(root, text="3", command=lambda: click(3), **button_style)
button_4 = Button(root, text="4", command=lambda: click(4), **button_style)
button_5 = Button(root, text="5", command=lambda: click(5), **button_style)
button_6 = Button(root, text="6", command=lambda: click(6), **button_style)
button_7 = Button(root, text="7", command=lambda: click(7), **button_style)
button_8 = Button(root, text="8", command=lambda: click(8), **button_style)
button_9 = Button(root, text="9", command=lambda: click(9), **button_style)
button_0 = Button(root, text="0", command=lambda: click(0), **button_style)
button_add = Button(root, text="+", command=add, **button_style)
button_subtract = Button(root, text="-", command=subtract, **button_style)
button_multiply = Button(root, text="*", command=multiply, **button_style)
button_divide = Button(root, text="/", command=divide, **button_style)
button_clear = Button(root, text="AC", command=clear, **button_style)
button_equal = Button(root, text="=", command=equal, **button_style)

# Arrange buttons on the grid
buttons = [
    (button_7, button_8, button_9, button_divide),
    (button_4, button_5, button_6, button_multiply),
    (button_1, button_2, button_3, button_subtract),
    (button_0, button_clear, button_equal, button_add),
]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        button.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

# Configure grid columns and rows to expand
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
