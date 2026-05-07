cap = 10
points = 0

print("welcome! please press enter to gain points or 'q' to quit")

while True:
    user_input = input()
    
    if user_input == "q":
        break
    
    points += 1
    
    print("You have gained a point")
    
    if points == cap:
        print("Good job! You've reached the point cap.")
        
        cap += 10
        points = 0
        print(f"New point cap is {cap}. Keep going!")
        