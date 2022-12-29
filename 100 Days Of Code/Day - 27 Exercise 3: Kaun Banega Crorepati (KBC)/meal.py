import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Meal Management")

        # Dictionary to store the students' meal balances
        self.students = {
            "Alice": 100,
            "Bob": 50,
            "Charlie": 75
        }

        # Create the widgets
        self.label = tk.Label(master, text="Enter student name:")
        self.entry = tk.Entry(master)
        self.check_balance_button = tk.Button(master, text="Check Balance", command=self.check_balance)
        self.add_money_button = tk.Button(master, text="Add Money", command=self.add_money)
        self.charge_meal_button = tk.Button(master, text="Charge Meal", command=self.charge_meal)
        self.output_label = tk.Label(master, text="")

        # Place the widgets in the window
        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.check_balance_button.grid(row=1, column=0)
        self.add_money_button.grid(row=1, column=1)
        self.charge_meal_button.grid(row=1, column=2)
        self.output_label.grid(row=2, column=0, columnspan=3)

    def check_balance(self):
        name = self.entry.get()
        if name in self.students:
            self.output_label.config(text=f"{name} has a balance of Rs. {self.students[name]}.")
        else:
            self.output_label.config(text=f"Error: Student {name} not found.")

    def add_money(self):
        name = self.entry.get()
        if name in self.students:
            self.students[name] += 50
            self.output_label.config(text=f"Rs. 50 added to {name}'s balance. New balance: Rs. {self.students[name]}.")
        else:
            self.output_label.config(text=f"Error: Student {name} not found.")

    def charge_meal(self):
        name = self.entry.get()
        if name in self.students:
            if self.students[name] >= 50:
                self.students[name] -= 50
                self.output_label.config(text=f"Rs. 50 charged to {name}'s balance. New balance: Rs. {self.students[name]}.")
            else:
                self.output_label.config(text=f"Error: Insufficient balance for {name}.")
        else:
            self.output_label.config(text=f"Error: Student {name} not found.")

# Create the main window
root = tk.Tk()

# Create an instance of the App class
app = App(root)

# Run the Tkinter event loop
root.mainloop()
