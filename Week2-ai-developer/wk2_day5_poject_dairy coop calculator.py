"""
Dairy Co-op Payment Calculator
-------------------------------
Farmer enters their name and litres supplied.
Tool shows total owed at current buying price.

Usage:
    python dairy_calculator.py

Config:
    Edit current_price in the script to update the weekly rate.
    Future version: read from price.txt
"""

def get_current_price():
    """Read current price from price.txt, fall back to default."""
    try:
        with open("price.txt", "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 75  # Default: KES 55 per litre


def calculate_payment(litres, price_per_litre):
    return litres * price_per_litre


def run():
    print("Kiambu Dairy Co-op Payment Calculator")
    print("--------------------------------------")
    print(f"Current buying price: KES {get_current_price():.2f} per litre")
    print()

    name = input("Farmer name: ").strip()
    if not name:
        print("Name is required.")
        return

    try:
        litres = float(input("Litres supplied today: "))
        if litres <= 0:
            print("Litres must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number for litres.")
        return

    price = get_current_price()
    total = calculate_payment(litres, price)

    print()
    print(f"Farmer : {name}")
    print(f"Litres : {litres}")
    print(f"Price  : KES {price:.2f}/litre")
    print(f"Total  : KES {total:,.2f}")


run()