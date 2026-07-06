def get_discount(age, is_member):
    if age > 60 and is_member:
        return "30% Discount"
    elif age > 60 and not is_member:
        return "20% Discount"
    elif age < 18 and is_member:
        return "20% Discount"
    elif age < 18 and not is_member:
        return "10% Discount"
    else:
        return "No Discount"


# Get user input
age = int(input("Enter Age: "))
member = input("Are you a member? (yes/no): ").lower()

# Convert input to Boolean
is_member = True if member == "yes" else False

# Get and display discount
result = get_discount(age, is_member)
print(f"Discount: {result}")