import random

print("Let's play Rock, Paper, Scissors!")
print("Enter your choice (rock, paper, or scissors) or 'quit' to exit: ")

score = {'user': 0, 'computer': 0, 'ties': 0}

while True:
    # take user input
    user_choice = input().lower()

    if user_choice == 'quit':
        break

    # generate computer's choice randomly
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    # determine the winner and update score
    if user_choice == computer_choice:
        print("It's a tie!")
        score['ties'] += 1
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win!")
            score['user'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("You win!")
            score['user'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("You win!")
            score['user'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1
    else:
        print("Invalid input! You must enter either rock, paper, or scissors.")

    # print current score
    print(f"\nCurrent score: User - {score['user']}, Computer - {score['computer']}, Ties - {score['ties']}\n")

print("Thanks for playing!")