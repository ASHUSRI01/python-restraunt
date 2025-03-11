import tkinter as tk

# Define the menu of the restaurant with item prices
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Dictionary to keep track of the quantities of each item
order_quantities = {item: 0 for item in menu}

# Create the main window
root = tk.Tk()
root.title("Python Restaurant")
root.geometry("400x600")

# Variable to store the total order amount
order_total = 0

def add_item(item_name):
    global order_total
    order_quantities[item_name] += 1
    order_total += menu[item_name]
    quantity_label[item_name].config(text=f"Qty: {order_quantities[item_name]}")

def show_total():
    global order_total
    bill_text.set("Python Restaurant\n---------------------------\n")
    for item, qty in order_quantities.items():
        if qty > 0:
            bill_text.set(bill_text.get() + f"{item}: {qty} x Rs {menu[item]} = Rs {qty * menu[item]}\n")
    bill_text.set(bill_text.get() + "---------------------------\n")
    bill_text.set(bill_text.get() + f"Total: Rs {order_total}")

# Create a label for the menu
menu_label = tk.Label(root, text="Welcome to PYTHON Restaurant\nMenu:", font=("Helvetica", 16))
menu_label.pack(pady=10)

# Frame to hold the menu items and their quantities
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

quantity_label = {}

# Display the menu items with buttons to increase quantity
for item, price in menu.items():
    item_frame = tk.Frame(menu_frame)
    item_frame.pack(fill="x", pady=5)
    
    tk.Label(item_frame, text=f"{item}: Rs {price}", font=("Helvetica", 14)).pack(side="left", padx=10)
    
    qty_label = tk.Label(item_frame, text=f"Qty: {order_quantities[item]}", font=("Helvetica", 12))
    qty_label.pack(side="left", padx=10)
    
    quantity_label[item] = qty_label
    
    add_button = tk.Button(item_frame, text="Add", font=("Helvetica", 12), command=lambda item=item: add_item(item))
    add_button.pack(side="right", padx=10)

# Show total button and label
bill_text = tk.StringVar()
bill_label = tk.Label(root, textvariable=bill_text, font=("Helvetica", 12), justify="left")
bill_label.pack(pady=10)

total_button = tk.Button(root, text="Show Total", font=("Helvetica", 14), command=show_total)
total_button.pack(pady=10)

root.mainloop()
