health = 100

def change_health(current_health, action):
    if action == "hit":
        return current_health - 10
    elif action == "heal":
        return current_health + 10
    else:
        return current_health
while True:
    user = input("Enter text the way you want to change the health or q to exit: ")
    if user == "q":
        exit()
    health = change_health(health, user)
    print(f"Your health is now {health}.")
    
    
    # import random
    # action = random.choice(["hit", "heal"])
    # to make random actions
    #
    #
    #
    #