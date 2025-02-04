"""
Author: [Felipe Zardo]

Purpose: Meal Price Calculator
Added Feature: Optional tip percentage for the meal total.

This program calculates the total price of a meal, including sales tax and optional tips,
and computes the change to give back to the customer after payment.
"""

# Milestone requirements
# Input prices and quantities
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

# Calculate the subtotal
subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

# Final requirements
# Input the sales tax rate
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))

# Calculate the sales tax
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate the total
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# Additional feature: Optional tip
tip_percentage = float(input("\nEnter a tip percentage (enter 0 for no tip): "))
tip = total * (tip_percentage / 100)
total_with_tip = total + tip
print(f"Tip: ${tip:.2f}")
print(f"Total with Tip: ${total_with_tip:.2f}")

# Input the payment amount
payment_amount = float(input("\nWhat is the payment amount? "))

# Calculate the change
change = payment_amount - total_with_tip
print(f"Change: ${change:.2f}")
