import random
import sys
while True:
    print(":)>>>WELCOME TO THE NUMBER GUESSING GAME<<<(:")
    print("The point of the game is to guess a number between 1-10, if you guess it correctly you WIN!")               
    print("You have 5 attempts") 
    print("Lets begin:")
    gen = random.randint(1,10)
    count = 1
    while True:
        num = input("Choose a number between 1-10  ")
        try:
            num = int(num)
            if num >= 11:
                raise ValueError
        except ValueError:
            print("Hmmmm, that's not an acceptable value !!!")
        else:
            if num == gen:
                print("YOU ARE CORRECT, YOU ARE A CHAMP")
                again = input("Do you want to play again CHAMP! ")
                if again == "yes":
                    break
                elif again == "no":    
                    print("GAME OVER")
                    sys.exit()
            elif count == 5:
                print("GAME OVER")
                again = input("Do you want to play again CHAMP! ")
                if again == "yes":
                    break
                elif again == "no":    
                    print("GAME OVER")
                    sys.exit()
            elif num <= gen:
                print("CLOSE!... a little higher por favor")
                count = count+1
                continue
            elif num >= gen:
                print("CLOSE!... a little lower por favor")
                count = count+1
                continue

