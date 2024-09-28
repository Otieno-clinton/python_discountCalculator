def calculate_discount(price, discount_percent):
    #Calculate the final price after applying a discount.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # No discount applied

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if final_price != original_price:
    print("The final price after applying the discount is: " +str(final_price))
else:
    print("No discount applied. The original price is: " + str(original_price))
