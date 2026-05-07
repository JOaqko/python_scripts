health = 10
quit = input("Press q to quit or any other key to continue: ")
if quit == "q":
    exit()
while True:
    print("Welcome! you are walking through a forest, but the road divides into two paths.")
    path = input("Do you want to go left or right? (l/r): ")
    if path == "l":
        print("You go throgh the left path and find a treasure chest!")
        decision1 = input("Do you want to open it? (y/n): ")
        if decision1 == "y":
            health += 20
            print("You opened the chest and found a health potion! Health increased by 20.")
        else:
            print("You chose not to open the chest. You continue on your way.")
    elif path == "r":
        print("You have chosen the right path, but you feel a little dizzy.")
        decision2 = input("Do you want to continue? (y/n): ")
        if decision2 == "y":
            health -= 1000
            if health <= 0:
                print("You have lost all your health because of a spell! Game over.")
                break
        else:
            print("You decided to turn back")
    