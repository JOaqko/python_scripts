health = 100

def change_health(current_health, action):
    actions = {
        "hit": current_health - 10,
        "heal": current_health + 10
    }
    return actions.get(action, current_health)
while True:
    print(f"Health: {health}")
    user = input("Enter a text the way that chnage the health or press q to quit: ")
    if user == "q":
        exit()
    health = change_health(health, user)