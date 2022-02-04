


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
# Extra Credit No. 2
def determine_winner(user_choice, computer_choice):
    if (user_choice == computer_choice):
        winner = None
    if (user_choice == "rock"):
        if (computer_choice =="paper"):
            winner = "paper"
        if (computer_choice == "scissors"):
            winner = "rock"
    if (user_choice == "paper"):
        if (computer_choice =="rock"):
            winner = "paper"
        if (computer_choice == "scissors"):
            winner = "scissors"
    if (user_choice == "scissors"):
        if (computer_choice =="rock"):
            winner = "rock"
        if (computer_choice == "paper"):
            winner = "scissors"
    return winner
if __name__ == "__main__":
    #EXTRA CREDIT No. 1
    import os

    player_name = os.getenv("PLAYER_NAME", default="Player One")

    # introduction
    print("Welcome to the Game!")
    print("Please follow all instructions henceforth outlined")
    #ask user for input
    user_input = input("Choose 'rock','paper','scissors':")
    print("You Chose:", user_input)

    #validate user input
    userChoice = user_input.lower()


    #computer choice
    import random
    options = ["rock","paper","scissors"]
    computerChoice = random.choice(options)
    print("Computer chooses:", computerChoice)

    #Winner Determination (through function)
    winner = determine_winner(userChoice, computerChoice)

    #determine winner 
   # if (userChoice == computerChoice):
   #     print("Game is a tie!")
   #     print("-------------------")
   #     print("Thanks for playing.")
  #  if((userChoice == "rock" and computerChoice == "paper") or (userChoice == "paper" and
   # computerChoice == "scissors") or (userChoice == "scissors" and computerChoice == "rock")):
    #    print("The computer won :(")
    #    print("-------------------")
    #    print("Thanks for playing.")
   # if((userChoice == "paper" and computerChoice == "rock") or (userChoice == "scissors" and
    #computerChoice == "paper") or (userChoice == "rock" and computerChoice == "scissors")):
     #   print("Congrats, you won! :)")
   #     print("-------------------")
    #    print("Thanks for playing.")
    
    if (winner == None):
        print("Game is a tie!")
    if (winner == computerChoice):
        print("Computer wins :(")
    if (winner == userChoice):
        if (player_name == "Player One"):
            print ("You Win!! :)")
        else:
            print(player_name, "wins! :")


    






