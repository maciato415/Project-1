import random
import sys

highscore = [5]

while True:
    print(":)>>>WELCOME TO THE NUMBER GUESSING GAME<<<(:")
    print("The point of the game is to guess a number between 1-10, if you guess it correctly you WIN!")               
    print("You have 5 attempts") 
    print("The HIGHSCORE is...")
    print(min(highscore))
    print("Lets begin:")
    gen = random.randint(1,10)
    count = 1
    
    while True:
        num = input("Choose a number between 1-10  ")
        try:
            num = int(num)
            if num >= 11:
                raise ValueError
            if num <= 0:
                raise ValueError
        except ValueError:
            print("Hmmmm, that's not an acceptable value !!!")
        else:
            if num == gen:
                print("YOU ARE CORRECT, YOU ARE A CHAMP")
                print("It only took you {} attemp/s".format(count))
                highscore.append(count)
                again = input("Do you want to play again CHAMP! yes/no ")
                if again.lower() == "yes":
                    break
                else:   
                    print("GAME OVER")
                    sys.exit()
            elif count == 5:
                print("GAME OVER")
                again = input("Do you want to play again CHAMP! yes/no ")
                if again.lower()  == "yes":
                    break
                else:    
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
