import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("""  ____    _            _           _            _    
 | __ )  | | __ _  ___| | __   ___| | __ _  ___| | __
 |  _ \  | |/ _` |/ __| |/ /  / __| |/ _` |/ __| |/ /
 | |_) | | | (_| | (__|   <  \__ \ | (_| | (__|   < 
 |____/  |_|\__,_|\___|_|\_\ |___/_|\__,_|\___|_|\_\

  __        __         _                                     
  \ \      / /__  _ __| | _____ _   _  ___  _ __   ___  ___  
   \ \ /\ / / _ \| '__| |/ / _ \ | | |/ _ \| '_ \ / _ \/ __| 
    \ V  V / (_) | |  |   <  __/ |_| | (_) | | | |  __/\__ \ 
     \_/\_/ \___/|_|  |_|\_\___|\__, |\___/|_| |_|\___||___/ 
                                |___/                        

============================================================
♠ ♣ ♥ ♦            WELCOME TO THE TABLE            ♠ ♣ ♥ ♦
============================================================
You vs Dealer. Closest to 21 wins — go over, and you bust!
Type 'hit' to draw a card, or 'stand' to end your turn.
============================================================
""")
user_list = []
comp_list = []
game = True
def rangen(L):
    val = random.choice(cards)
    L.append(val)
    return L
def check(U, C):
    global Cmd
    Usum = sum(U)
    Csum = sum(C)
    print(f"your Deck: {U}, Sum: {Usum} Dealer Deck: {C}, Sum: {Csum}")
    input("Hit Enter to continue")
    if Usum == 21 or Csum > 21:
        print("Congratulations! You have won the game")
        Cmd = False
    elif Csum == 21 or Usum > 21:
        print("oh no you have lost the game :(")
        Cmd = False
def ask():
    decison = input("do you want to get Hit or Nah (y/n)")
    if decison == "y":
        rangen(user_list)
    rangen(comp_list)
    return decison
while game == True:
    choice = input("Do you want to play a game of blackjack?")
    if choice == "n":
        print("come again soon☺")
        break
    elif choice == "y":
        Cmd = True
        rangen(rangen(user_list))
        rangen(rangen(comp_list))
        print(f"This is your card: {user_list}")
        print(f"This is the Dealer card: {comp_list}")
        while Cmd == True:
            ask()
            check(user_list, comp_list)
        if Cmd == False:
            print("G A M E O V E R !")
    else:
        print("Invaid Input ☺")
        break
    
