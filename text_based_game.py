from unittest import case

player = {
    "health": 100,
    "stamina": 50
}

enemy = {
    "health": 80
}

def attack (player, enemy):
    player["stamina"] -= 10
    enemy["health"] -= 15
    if (player["stamina"] < 10):
        print("You are too tired to attack!")
        player["stamina"] = 0
     
def heal (player):
    player["stamina"] -= 15
    player["health"] += 15
    if (player["health"] > 100):
        player["health"] = 100

def rest (player):
    player["stamina"] += 20
    if (player["stamina"] > 50):
        player["stamina"] = 50

def main():
    while player["health"] > 0 and enemy["health"] > 0:
        print("Player Health: ", player["health"], ", Stamina: ", player["stamina"])
        print("Enemy Health: ", enemy["health"])

        print("Choose an action: 1) Attack 2) Heal 3) Rest 4) Quit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                attack(player, enemy)
            case "2":
                heal(player)
            case "3":
                rest(player)
            case "4":
                print("Thanks for playing!")
                break
            case default:
                print("Invalid choice, try again.")
        print("<-------The enemy attacks you!------->")
        player["health"] -= 8

        if player["health"] <= 0:
            print("You have been defeated!")
        elif enemy["health"] <= 0:
            print("You have defeated the enemy!")
if __name__ == "__main__":    main()
        

