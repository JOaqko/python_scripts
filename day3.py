weight = 10 #kg
limit = 100 #kg

print("Welcome! You have a weight limit of 100kg. Do not exceed it!")
while True:
    print(f"Current weight: {weight}kg")
    user_input = input("Press 'a' to add 5kg, 'r' to remove 5kg, or 'q' to quit: ")
    
    if user_input == "q":
        break
    elif user_input == "a":
        weight += 5
        print(f"Added 5kg. Current weight: {weight}kg")
    elif user_input == "r":
        weight -= 5
        print(f"Removed 5kg. Current weight: {weight}kg")
        
    if weight > limit:
        print("Weight limit exceeded! Resetting weight to 10kg.")
        weight = 10