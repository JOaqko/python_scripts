health = 100

def change_health(health_changes):
    if user1 == "hit":
        return health_changes - 10
    elif user1 == "heal":
        return health_changes + 10
    elif user1 == "q":
        exit()
    else:
        return "Invalid input, please enter 'hit' or 'heal'."
while True:
    print(f"Current health: {health}, enter hit or heal to change health or q to exit.")
    user1 = input()
    health = change_health(health)
    print(f"Your health is now {health}.")
    