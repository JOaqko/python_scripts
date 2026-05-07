players_level = 1
players_xp = 0

print("Welcome to the game! You have to gain XP to Level up. (Press 'q' to quit)")

while True:
    userI = input()
    
    if userI == 'q':
        break
    
    players_xp += 1
    print("You have gained XP")
    
    if players_xp == 3:
        players_level += 1
        players_xp = 0
        print("level up!")
    
    
    
    
    
    
    
