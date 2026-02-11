grand_total = 0  # This starts at zero

# This loop will run 5 times
for i in range(5):
    print(f"\nPerson {i+1}:")
    age = int(input("Enter age: "))
    
    # Logic to determine price
    if age < 12:
        price = 5
    elif age > 60:
        price = 8
    else:
        price = 12
        
    print(f"Ticket price for this person: ${price}")
    
    # Add the price to our running total
    grand_total += price

# After the loop finishes, print the final result
print("-" * 20)
print(f"The grand total for all tickets is: ${grand_total}")