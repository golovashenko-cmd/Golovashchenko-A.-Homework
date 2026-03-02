"""
Project: Receipts for Lovely Loveseats
Follow the instructions in the comments to build the receipt system.
"""

# --- Adding In The Catalog ---

# 1. Create a variable called lovely_loveseat_description and assign to it the string:
# "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
print(lovely_loveseat_description)


# 2. Create a variable lovely_loveseat_price and set it equal to 254.00.
lovely_loveseat_price = 254.00

# 3. Create a variable called stylish_settee_description and assign to it the string:
# "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# 4. Create a variable stylish_settee_price and assign it the value of 180.50.
stylish_settee_price = 180.50

# 5. Create a variable called luxurious_lamp_description and assign it the string:
# "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# 6. Create a variable called luxurious_lamp_price and set it equal to 52.15.
luxurious_lamp_price = 52.15

# 7. Define the variable sales_tax and set it equal to .088 (8.8%).
sales_tax = 0.088


# --- Our First Customer ---

# 8. Define a variable called customer_one_total and set it to 0.

customer_one_total = 0

# 9. Create a variable called customer_one_itemization and set it to an empty string "".
customer_one_itemization= ''

# 10. The customer decides to purchase the Lovely Loveseat. Add the price to customer_one_total.
customer_one_total += lovely_loveseat_price

# 11. Add the description of the Lovely Loveseat to customer_one_itemization.
customer_one_itemization += lovely_loveseat_description

# 12. The customer also decides to purchase the Luxurious Lamp. Add the price to the total.
customer_one_total += luxurious_lamp_price

# 13. Add the description of the Luxurious Lamp to customer_one_itemization.
customer_one_itemization += luxurious_lamp_description

# 14. Calculate sales tax by creating a variable customer_one_tax and setting it
# equal to customer_one_total times sales_tax.
customer_one_tax = customer_one_total * sales_tax


# 15. Add the sales tax to the customer’s total cost.
customer_one_total += customer_one_tax



# --- Printing the Receipt ---

# 16. Print the phrase "Customer One Items:".
print('Customer One Items:')

# 17. Print customer_one_itemization.
print(customer_one_itemization)

# 18. Print the phrase "Customer One Total:".
print('Customer One Total:')

# 19. Print customer_one_total.
print( round(customer_one_total,2))



