# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):

    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price by subtracting the discount amount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Main part of the program
if __name__ == "__main__":
    # Prompt the user to input the original price of the item in Ksh
    original_price = float(input("Enter the original price of the item in Ksh: "))
    
    # Prompt the user to input the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price after applying the discount
    if final_price != original_price:
        print(f"The final price after applying the discount is: Ksh {final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: Ksh {final_price:.2f}")
