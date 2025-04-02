# Creating a file
def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
    else:
        final_price = price
    
    return final_price

# Prompt user for input
original_price = float(input("70: "))
discount_percentage = float(input("20: "))

# Calculate and display final price
final_price = calculate_discount(original_price, discount_percentage)

print(f"The final price after applying the discount is: {final_price:.2f}")