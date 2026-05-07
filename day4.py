oxygen = 100 #percentage
outOfOxygen = 0 #percentage
health = 100 #percentage


print("Welcome! You can dive underwater. Monitor your oxygen levels carefully!")
user_input = input("Press q to quit or any other key to continue: ")
if user_input == "q":
    exit()

isUnderwater = input("Do you want to dive underwater? (y/n): ")

if isUnderwater == "y":
    while True:
        print(f"Current oxygen: {oxygen}%")
        print(f"Current health: {health}%")
        oxygen -= 10
        user_input = input("Press 's' to surface, or any other key to continue diving: ")
        if user_input == "s":
            print("You have surfaced safely!")
            break
        if oxygen <= outOfOxygen:
            health -= 20
            print("You have run out of oxygen! Health decreasing by 20%")
            if health <= 0:
                print("You have lost all your health! Game over.")
                break
            
        print("Diving deeper... Oxygen decreasing by 10%")
else:
    print("You chose not to dive. Stay safe!")
    

