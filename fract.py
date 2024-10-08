import tkinter as tk
from tkinter import messagebox

class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            self.denominator = 1
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        self.reduce()

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        return fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        return fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __pow__(self, exponent):
        if exponent >= 0:
            return fraction(pow(self.numerator, exponent), pow(self.denominator, exponent))
        else:
            return fraction(pow(self.denominator, -exponent), pow(self.numerator, -exponent))

    def reduce(self):
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        gcd_value = gcd(self.numerator, self.denominator)
        self.numerator //= gcd_value
        self.denominator //= gcd_value


def calculate(operation):
    try:
        num1 = int(entry_num1.get())
        denom1 = int(entry_denom1.get())
        num2 = int(entry_num2.get())
        denom2 = int(entry_denom2.get())
        
        frac1 = fraction(num1, denom1)
        frac2 = fraction(num2, denom2)
        
        if operation == '+':
            result = frac1 + frac2
        elif operation == '-':
            result = frac1 - frac2
        elif operation == '*':
            result = frac1 * frac2
        elif operation == '/':
            result = frac1 / frac2
        elif operation == '**':
            exponent = int(entry_exponent.get())
            result = frac1 ** exponent
        else:
            result = "Invalid Operation"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for numerators and denominators.")


root = tk.Tk()
root.title("Fraction Calculator")

tk.Label(root, text="Fraction 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=0)
tk.Label(root, text="⎯⎯⎯⎯⎯⎯⎯⎯⎯").grid(row=2, column=0)
entry_denom1 = tk.Entry(root)
entry_denom1.grid(row=3, column=0)


tk.Label(root, text="Fraction 2:").grid(row=0, column=1)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)
tk.Label(root, text="⎯⎯⎯⎯⎯⎯⎯⎯⎯").grid(row=2, column=1)
entry_denom2 = tk.Entry(root)
entry_denom2.grid(row=3, column=1)



tk.Label(root, text="Exponent:").grid(row=0, column=3)
entry_exponent = tk.Entry(root)
entry_exponent.grid(row=1, column=3)

tk.Button(root, text="+", command=lambda: calculate('+')).grid(row=5, column=0)
tk.Button(root, text="-", command=lambda: calculate('-')).grid(row=5, column=1)
tk.Button(root, text="*", command=lambda: calculate('*')).grid(row=5, column=2)
tk.Button(root, text="/", command=lambda: calculate('/')).grid(row=5, column=3)
tk.Button(root, text="**", command=lambda: calculate('**')).grid(row=2, column=3)

def key_pressed(event):
    if event.keysym == "Escape":
        root.quit()
    elif event.keysym == "Return":
        focus_next_widget(event.widget)
    

def focus_next_widget(widget):
    widget.tk_focusNext().focus()
    return "break"
        

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=6, column=0, columnspan=5)




root.bind("<Key>", key_pressed)
root.mainloop()