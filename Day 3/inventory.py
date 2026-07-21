# Pharmacy Inventory Tracker

stock = {}

# Read stock from file
try:
    with open("stock.txt", "r") as file:
        for line in file:
            item, qty = line.strip().split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("No stock file yet — starting empty.")

# Function to update stock
def adjust(item, amount):
    stock[item] = stock.get(item, 0) + amount

# Ask user for update
item = input("Enter item name: ")
amount = int(input("Enter quantity to add (+) or remove (-): "))

adjust(item, amount)

# Display current inventory
print("\nCurrent Inventory:")
for item, qty in stock.items():
    print(f"{item}: {qty}")

# Display low-stock items
low_stock = [item for item, qty in stock.items() if qty < 10]

print("\nLow Stock Items:")
if low_stock:
    for item in low_stock:
        print(item)
else:
    print("No low stock items.")

# Save updated stock back to file
with open("stock.txt", "w") as file:
    for item, qty in stock.items():
        file.write(f"{item},{qty}\n")

print("\nInventory updated and saved successfully.")