import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Initialize variables
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.current_number = ""
        self.first_number = 0
        self.operation = ""
        self.should_reset = False
        
        # Create display frame
        display_frame = tk.Frame(self.root, bg="#34495e")
        display_frame.pack(fill="x", padx=10, pady=10)

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 32, "bold"),
            bg="#34495e",
            fg="white",
            anchor="e",
            padx=20,
            pady=20
        )
        self.display.pack(fill="both", expand=True)
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Button configuration
        button_config = [
            ("C", "#e74c3c", "#c0392b"),
            ("±", "#95a5a6", "#7f8c8d"),
            ("%", "#95a5a6", "#7f8c8d"),
            ("÷", "#f39c12", "#e67e22"),
            ("7", "#34495e", "#2c3e50"),
            ("8", "#34495e", "#2c3e50"),
            ("9", "#34495e", "#2c3e50"),
            ("×", "#f39c12", "#e67e22"),
            ("4", "#34495e", "#2c3e50"),
            ("5", "#34495e", "#2c3e50"),
            ("6", "#34495e", "#2c3e50"),
            ("-", "#f39c12", "#e67e22"),
            ("1", "#34495e", "#2c3e50"),
            ("2", "#34495e", "#2c3e50"),
            ("3", "#34495e", "#2c3e50"),
            ("+", "#f39c12", "#e67e22"),
            ("0", "#34495e", "#2c3e50", 2),  # Span 2 columns
            (".", "#34495e", "#2c3e50"),
            ("=", "#27ae60", "#229954")
        ]
        
        # Create buttons
        row = 0
        col = 0
        for i, config in enumerate(button_config):
            if len(config) == 4:  # Button spans multiple columns
                text, bg_color, active_color, colspan = config
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg="white",
                    activebackground=active_color,
                    activeforeground="white",
                    relief="flat",
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")
                col += colspan
            else:
                text, bg_color, active_color = config
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg="white",
                    activebackground=active_color,
                    activeforeground="white",
                    relief="flat",
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                col += 1
            
            if col >= 4:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value.isdigit() or value == ".":
            self.handle_number(value)
        elif value in ["+", "-", "×", "÷"]:
            self.handle_operator(value)
        elif value == "=":
            self.calculate()
        elif value == "C":
            self.clear()
        elif value == "±":
            self.toggle_sign()
        elif value == "%":
            self.percentage()
    
    def handle_number(self, number):
        if self.should_reset:
            self.current_number = ""
            self.should_reset = False
        
        if number == "." and "." in self.current_number:
            return
        
        self.current_number += number
        self.display_var.set(self.current_number)
    
    def handle_operator(self, operator):
        if self.current_number:
            if self.operation and not self.should_reset:
                self.calculate()
            
            self.first_number = float(self.current_number)
            self.operation = operator
            self.should_reset = True
        elif self.operation and self.should_reset:
            # Change operation
            self.operation = operator
    
    def calculate(self):
        if not self.current_number or not self.operation:
            return
        
        second_number = float(self.current_number)
        result = 0
        
        if self.operation == "+":
            result = self.first_number + second_number
        elif self.operation == "-":
            result = self.first_number - second_number
        elif self.operation == "×":
            result = self.first_number * second_number
        elif self.operation == "÷":
            if second_number == 0:
                self.display_var.set("Error")
                return
            result = self.first_number / second_number
        
        # Format result
        if result.is_integer():
            result = int(result)
        
        self.display_var.set(str(result))
        self.current_number = str(result)
        self.operation = ""
        self.should_reset = True
    
    def clear(self):
        self.current_number = ""
        self.first_number = 0
        self.operation = ""
        self.should_reset = False
        self.display_var.set("0")
    
    def toggle_sign(self):
        if self.current_number and self.current_number != "0":
            if self.current_number.startswith("-"):
                self.current_number = self.current_number[1:]
            else:
                self.current_number = "-" + self.current_number
            self.display_var.set(self.current_number)
    
    def percentage(self):
        if self.current_number:
            value = float(self.current_number)
            result = value / 100
            if result.is_integer():
                result = int(result)
            self.current_number = str(result)
            self.display_var.set(self.current_number)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 