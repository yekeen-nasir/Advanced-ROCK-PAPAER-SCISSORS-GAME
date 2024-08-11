import random

print("rock!""\n" "paper!!" "\n" "scissors!!!")
player_name=input("enter your name:")
print("welcome to the game ",player_name)    



# starting the game 
def game():
    playerscore = 0
    systemscore = 0
    player_total_score = 0
    system_total_score = 0
    # our program        
    x=1
    while x <=3:
        x +=1
        player=input("choose \"rock,paper,scissors:")
        sysgame=["rock","paper","scissors"]
        system_player=random.choice(sysgame)
        print("system_player: ",system_player)
        print(" ")
        if player in sysgame: 
            #for player
            if player == system_player:
                print("its a draw!!")
                draw = "its a draw"
                if draw == "its a draw":
                    playerscore = 0
                    systemscore = 0
            elif player=="scissors" and system_player=="paper":
                print("you win!!!!!!")
                you_win = "you win!!!!!!"
                if you_win == "you win!!!!!!":
                    playerscore = 1
                    if playerscore == 1:
                         systemscore = 0
            elif player=="rock" and system_player=="scissors":
                print("you win!!!!!")
                you_win = "you win!!!!!!"
                if you_win == "you win!!!!!!":
                    playerscore = 1
                    if playerscore == 1:
                        systemscore = 0
            elif player=="paper" and system_player=="rock":
                print("you win!!!!!")
                you_win = "you win!!!!!!"
                if you_win == "you win!!!!!!":
                    playerscore = 1
                    if playerscore == 1:
                        systemscore = 0
        #for system
            elif system_player=="scissors" and player=="paper":
                print("system wins!!!!!!")
                system_win = "system wins!!!!!!"
                if system_win == "system wins!!!!!!":
                    systemscore = 1
                    if systemscore == 1:
                        playerscore = 0
            elif system_player=="rock" and player=="scissors":
                print("system wins!!!!!")
                system_win = "system wins!!!!!!"
                if system_win == "system wins!!!!!!":
                    systemscore = 1
                    if systemscore == 1:
                        playerscore = 0
            elif system_player=="paper" and player=="rock":
                print("system wins!!!!!")
                system_win = "system wins!!!!!!"
                if system_win == "system wins!!!!!!":
                    systemscore = 1
                    if systemscore == 1:
                        playerscore = 0
        else:
            print("invalid choice")
        player_total_score += playerscore
        system_total_score += systemscore
        print("FOR SYSTEM:",system_total_score,"\n",player_name,":",player_total_score)
        if system_total_score == player_total_score:
            print("It's a tie🤔🤔🤔")
        elif system_total_score > player_total_score:
            print("You Loose😥😓😓")
        elif system_total_score < player_total_score:
            print("You win!!!!!🕺💃🕺💃") 

#                       
decision = input("Press enter to start the Rock|Paper|Scissors Game")
if decision == "":
    print("Let's Play!!!🎈🎈🎈")
    game()
    gameagain = input("DO You want to play again? (Yes || No)")
    if gameagain == "yes" or "Yes" or "YES":
        game()
    elif gameagain() == "no" or "No" or "NO":
        print("Program Terminated.....................")
        print("Thanks for Playing")
        print("ENJOY YOUR DAY!")
    else:
        print("Program Terminated....................................")    
else:
    decision2 = input("Player "+ player_name + ", Just click on the  ENTER key")
    if decision2 == "":
        print("Let's Play!!!🎈🎈🎈")
        game()
        gameagain = input("DO You want to play again? (Yes || No)")
        if gameagain == "yes" or "Yes" or "YES":
            game()
        elif gameagain() == "no" or "No" or "NO": 
            print("Program Terminated.....................")
            print("Thanks for Playing")
            print("ENJOY YOUR DAY!")
        else:
            print("Program Terminated....................................")    
    else:
        print("""YOU WON'T LISTEN
               PROGRAM TERMINATED!!!!!!!!""")
        again = input("Hope you  will like to follow the rules this time? (Yes || No)")
        if again == "yes" or "Yes" or "YES":
            game()
        elif again == "no" or "No" or "NO":
            print("Program Terminated.....................")
            print("ENJOY YOUR DAY!")
        else:
            print("Program Terminated....................................")




