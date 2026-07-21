# =========================
# Exercise 1: Unique Cities
# =========================

cities = ["Addis Ababa", "Mekelle", "Adama", "Addis Ababa", "Mekelle"]

unique_cities = set(cities)

print("Unique Cities:", unique_cities)
print("Number of Unique Cities:", len(unique_cities))


# =========================
# Exercise 2: Price Report
# =========================

grocery = {
    "Bread": 40,
    "Milk": 90,
    "Sugar": 120,
    "Rice": 250,
    "Eggs": 180
}

print("\nPrice Report")
for item, price in grocery.items():
    print(f"{item}: {price} ETB")


# =========================
# Exercise 3: Tax Comprehension
# =========================

prices = [100, 250, 400, 80]

tax_prices = [price * 1.15 for price in prices]

print("\nPrices with 15% Tax:")
print(tax_prices)


# =========================
# Exercise 4: Cheap Items
# =========================

cheap_items = [price for price in prices if price < 200]

print("\nPrices Under 200 ETB:")
print(cheap_items)


# =========================
# Exercise 5: Write & Read File
# =========================

with open("names.txt", "w") as file:
    file.write("Abebe\n")
    file.write("Mahder\n")
    file.write("Sara\n")

print("\nCustomer Names:")

with open("names.txt", "r") as file:
    for name in file:
        print(name.strip())


# =========================
# Exercise 6: Safe Division
# =========================

try:
    number = float(input("\nEnter a number: "))
    result = 1000 / number
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")