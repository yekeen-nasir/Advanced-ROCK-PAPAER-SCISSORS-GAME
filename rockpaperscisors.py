import random

print("rock!""\n" "paper!!" "\n" "scissors!!!")
def systemgame():
    player_name=input("enter your name:")
    while player_name == "" or player_name == " " or player_name == "  " or player_name == "   ":
        player_name=input("enter your name:")
    print("welcome to the game ",player_name)    
# starting the game 
    def game():
        playerscore = 0
        systemscore = 0
        player_total_score = 0
        system_total_score = 0
    # our program        
        x=0
        while x <3:
            x +=1
        # last = "____________________________ ROUND", x,"__________________________"
            if x == 3:
                print("____________________________ LAST ROUND __________________________")
            else:
                print("____________________________ ROUND", x,"__________________________")
            player=input("choose \"rock,paper,scissors\":")
            sysgame=["rock","paper","scissors"]
            while player not in sysgame:
                player=input("choose \"rock,paper,scissors\":")
            system_player=random.choice(sysgame)
            print("system_player: ",system_player)
            if player in sysgame: 
            #for player
                if player == system_player:
                    print("its a draw!!")
                    print("     ")
                    draw = "its a draw"
                    if draw == "its a draw":
                        playerscore = 0
                        systemscore = 0
                elif player=="scissors" and system_player=="paper":
                    print("you win!!!!!!")
                    print("     ")
                    you_win = "you win!!!!!!"
                    if you_win == "you win!!!!!!":
                        playerscore = 1
                        if playerscore == 1:
                             systemscore = 0
                elif player=="rock" and system_player=="scissors":
                    print("you win!!!!!")
                    print("     ")
                    you_win = "you win!!!!!!"
                    if you_win == "you win!!!!!!":
                        playerscore = 1
                        if playerscore == 1:
                            systemscore = 0
                elif player=="paper" and system_player=="rock":
                    print("you win!!!!!")
                    print("     ")
                    you_win = "you win!!!!!!"
                    if you_win == "you win!!!!!!":
                        playerscore = 1
                        if playerscore == 1:
                            systemscore = 0
        #for system
                elif system_player=="scissors" and player=="paper":
                    print("system wins!!!!!!")
                    print("     ")
                    system_win = "system wins!!!!!!"
                    if system_win == "system wins!!!!!!":
                        systemscore = 1
                        if systemscore == 1:
                            playerscore = 0
                elif system_player=="rock" and player=="scissors":
                    print("system wins!!!!!")
                    print("     ")
                    system_win = "system wins!!!!!!"
                    if system_win == "system wins!!!!!!":
                        systemscore = 1
                        if systemscore == 1:
                            playerscore = 0
                elif system_player=="paper" and player=="rock":
                    print("system wins!!!!!")
                    print("     ")
                    system_win = "system wins!!!!!!"
                    if system_win == "system wins!!!!!!":
                        systemscore = 1
                        if systemscore == 1:
                            playerscore = 0
            else:
                print("invalid choice")
                continue
            player_total_score += playerscore
            system_total_score += systemscore
            print("SYSTEM:",system_total_score,"  ||  ",player_name.upper(),":",player_total_score)
        if system_total_score == player_total_score:
            print("                    It's a tie🤔🤔🤔")
        elif system_total_score > player_total_score:
            print("                    You Lost the Game😝😝😝")
        elif system_total_score < player_total_score:
            print("                    You won the Game!!!🕺💃🕺💃") 
    gameagain = ""
    decision = input("Press enter to start the Rock|Paper|Scissors Game ")
    while decision != "exit" or decision != "exit" or decision != "EXIT":
        if decision == ""  or gameagain == "yes" or gameagain == "Yes" or gameagain == "YES":
            print("Let's Play!!!🎈🎈🎈")
            game()
            gameagain = input("DO You want to play again? (Yes || No)")
            if gameagain == "yes" or gameagain == "Yes" or gameagain == "YES":
                print("Let's Play!!!🎈🎈🎈")
                game()
            elif gameagain == "no" or gameagain == "No" or gameagain == "NO":
                print("Program Terminated.....................")
                print("Thanks for Playing")
                print("ENJOY YOUR DAY!")
                break
            else:
                print("Program Terminated....................................")    
                break
            gameagain = input("DO You want to play again? (Yes || No)")
            decision = "lol"
        elif gameagain == "no" or gameagain == "No" or gameagain == "NO":
                print("Program Terminated.....................")
                print("Thanks for Playing")
                print("ENJOY YOUR DAY!")
                break
        else:
            decision = input("Player "+ player_name + ", Just click on the  ENTER key ")
            if decision == "":
                print("Let's Play!!!🎈🎈🎈")
                game()
                if gameagain == "yes" or gameagain ==  "Yes" or gameagain == "YES":
                    print("Let's Play!!!🎈🎈🎈")
                    game()
                elif gameagain == "no" or gameagain == "No" or gameagain == "NO":
                    print("Program Terminated.....................")
                    print("Thanks for Playing")
                    print("ENJOY YOUR DAY!")
                    break
                else:
                    print("Program Terminated....................................")    
                    break
                gameagain = input("DO You want to play again? (Yes || No)")
                decision = "lol"
            else:
                print("""YOU WON'T LISTEN
                   PROGRAM TERMINATED!!!!!!!!""")
                again = input("Hope you  will like to follow the rules this time? (Yes || No)")
                if again == "yes" or again == "Yes" or again == "YES":
                    print("Let's Play!!!🎈🎈🎈")
                    game()
                elif again == "no" or again == "No" or again == "NO":
                    decision = "exit"
                    print("Program Terminated.....................")
                    print("ENJOY YOUR DAY!")
                    break
                else:
                    print("Program Terminated....................................")
                    break
                gameagain = input("DO You want to play again? (Yes || No)")
                decision = "lol"
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
# HUMAN GAME..........HUMAN GAME...........HUMAN GAME................FUNCTION
print("Welcome to the Game guys!!!")
def humangame():
    player_Aname = input("First Player's Name: ")
    while player_Aname == "":
        player_Aname=input("First Player's Name: ")
    player_Bname = input("Second Player's Name: ")
    while player_Bname == "":
        player_Bname=input("Second Player's Name: ")
    print("welcome to the game ",player_Bname, "and", player_Aname)    
# starting the game 
    def game():
        player_A_score = 0
        player_B_score = 0
        playerA_total_score = 0
        playerB_total_score = 0
        # our program        
        x=0
        while x <3:
            x +=1
        # last = "____________________________ ROUND", x,"__________________________"
            if x == 3:
                print("____________________________ LAST ROUND __________________________")
            else:
                print("____________________________ ROUND", x,"__________________________")
            sysgame=["rock","paper","scissors"]
            print(player_Aname, end=":")
            playerA=input("choose \"rock,paper,scissors\":")
            while playerA not in sysgame:
                print(player_Aname, end=":")
                playerA=input("choose \"rock,paper,scissors\":")
            print(player_Bname, end=":")
            playerB=input("choose \"rock,paper,scissors\":")
            while playerB not in sysgame:
                print(player_Bname, end=":")
                playerB=input("choose \"rock,paper,scissors\":")
            if playerA in sysgame or playerB in sysgame: 
            #for first player
                if playerA == playerB:
                    print("its a draw!!")
                    print("     ")
                    draw = "its a draw"
                    if draw == "its a draw":
                        player_A_score = 0
                        player_B_score = 0
                elif playerA =="scissors" and playerB =="paper":
                    print( player_Aname, "win!!!!!!")
                    print("     ")
                    player_A = "you win!!!!!!"
                    if player_A == "you win!!!!!!":
                        player_A_score = 1
                        if player_A_score == 1:
                            player_B_score = 0
                elif playerA =="rock" and playerB =="scissors":
                    print(player_Aname,"win!!!!!")
                    print("     ")
                    player_A = "you win!!!!!!"
                    if player_A == "you win!!!!!!":
                        player_A_score = 1
                        if player_A_score == 1:
                            player_B_score = 0
                elif playerA =="paper" and playerB =="rock":
                    print(player_Aname,"win!!!!!")
                    print("     ")
                    player_A = "you win!!!!!!"
                    if player_A == "you win!!!!!!":
                        player_A_score = 1
                        if player_A_score == 1:
                            player_B_score = 0
        #for second player
                elif playerB =="scissors" and playerA =="paper":
                    print( player_Bname, "win!!!!!!")
                    print("     ")
                    player_B = "you win!!!!!!"
                    if player_B == "you win!!!!!!":
                        player_B_score = 1
                        if player_B_score == 1:
                            player_A_score = 0
                elif playerB =="rock" and playerA =="scissors":
                    print(player_Bname,"win!!!!!")
                    print("     ")
                    player_B = "you win!!!!!!"
                    if player_B == "you win!!!!!!":
                        player_B_score = 1
                        if player_B_score == 1:
                            player_A_score = 0
                elif playerB =="paper" and playerA =="rock":
                    print(player_Bname,"win!!!!!")
                    print("     ")
                    player_B = "you win!!!!!!"
                    if player_B == "you win!!!!!!":
                        player_B_score = 1
                        if player_B_score == 1:
                            player_A_score = 0
            else:
                print("invalid choice")
                continue
            playerA_total_score += player_A_score
            playerB_total_score += player_B_score
            print(player_Aname.upper(),playerA_total_score,"  ||  ",player_Bname.upper(),":",playerB_total_score)
        if playerA_total_score == playerB_total_score:
            print("                    It's a tie🤔🤔🤔")
        elif playerA_total_score > playerB_total_score:
            print("                     ",player_Aname, end=" ")
            print("Won the Game😝😝😝")
        elif playerA_total_score < playerB_total_score:
            print("                     ",player_Bname, end=" ")
            print("won the Game!!!🕺💃🕺💃") 



    gameagain = ""
    decision = input("Press enter to start the Rock|Paper|Scissors Game ")
    while decision != "exit" or decision != "exit" or decision != "EXIT":
        if decision == ""  or gameagain == "yes" or gameagain == "Yes" or gameagain == "YES":
            print("Let's Play!!!🎈🎈🎈")
            game()
            gameagain = input("DO You want to play again? (Yes || No)")
            if gameagain == "yes" or gameagain == "Yes" or gameagain == "YES":
                print("Let's Play!!!🎈🎈🎈")
                game()
            elif gameagain == "no" or gameagain == "No" or gameagain == "NO":
                print("Program Terminated.....................")
                print("Thanks for Playing")
                print("ENJOY YOUR DAY!")
                break
            else:
                print("Program Terminated....................................")    
                break
            gameagain = input("DO You want to play again? (Yes || No)")
            decision = "lol"
        elif gameagain == "no" or gameagain == "No" or gameagain == "NO":
            print("Program Terminated.....................")
            print("Thanks for Playing")
            print("ENJOY YOUR DAY!")
            break
        else:
            decision = input("Dear Players, one of you should click on the  ENTER key ")
            if decision == "":
                print("Let's Play!!!🎈🎈🎈")
                game()
                if gameagain == "yes" or gameagain ==  "Yes" or gameagain == "YES":
                    print("Let's Play!!!🎈🎈🎈")
                    game()
                elif gameagain == "no" or gameagain == "No" or gameagain == "NO":
                    print("Program Terminated.....................")
                    print("Thanks for Playing")
                    print("ENJOY YOUR DAY!")
                    break
                else:
                    print("Program Terminated....................................")    
                    break
                gameagain = input("DO You want to play again? (Yes || No)")
                decision = "lol"
            else:
                print("""YOU WON'T LISTEN
               PROGRAM TERMINATED!!!!!!!!""")
                again = input("Hope you  will like to follow the rules this time? (Yes || No)")
                if again == "yes" or again == "Yes" or again == "YES":
                    print("Let's Play!!!🎈🎈🎈")
                    game()
                elif again == "no" or again == "No" or again == "NO":
                    decision = "exit"
                    print("Program Terminated.....................")
                    print("ENJOY YOUR DAY! and kindly Fuck Off")
                    break
                else:
                    print("Program Terminated....................................")
                    print("ENJOY YOUR DAY! and kindly Fuck Off")
                    break
                gameagain = input("DO You want to play again? (Yes || No)")
                decision = "lol"

print("Welcome to the game!")
print("Choose option A or B")
# playerdecision = input("Player Vs Player(A) || Player Vs Computer(B) ")
while 1:
    playerdecision = input("Player Vs Player(A) || Player Vs Computer(B) ")
    if (playerdecision == 'x'):
        print('program terminated')
        break

    if "b" in playerdecision:
        systemgame()
    elif "a" in playerdecision:
        print("Welcome to the Game guys!!!")
        humangame()
    else:
        print('wrong key entered, try again or enter x to terminate')
        # print("try again? a || b")
        # if "a":
        #     humangame()
        # elif "b":
        #     systemgame()
        # else:

