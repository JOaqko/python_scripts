health = 100

def change_health(current_health, action):
    actions = {
        "damage": current_health - 1,
    }
    return actions.get(action, current_health)

while True:
    print(f"Health: {health}")
    if health <= 0:
        print("You are dead!")
        break
    health = change_health(health, "damage")
    
    