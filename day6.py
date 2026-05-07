gold = 50
def add_gold(current_gold):
    return current_gold + 10

while True:
    userI = input("Do you want to add 10 gold? or enter 'q' to quit: ")
    if userI == 'q':
        break
    gold = add_gold(gold)
    print(f"You now have {gold} gold.")
    
    

    
    

    
     
