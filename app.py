import random

game_value = ["🪨", "📄", "✂️"]


while True:



    def get_user_choice():
        while True:
            user_choice = str(input("Rock paper or scissors?(r/p/s)")).lower()
            if user_choice in ("r", "p", "s"):
                break

    continue_ask = (input("Do you want to play? y/n")).lower()



    if continue_ask == "n":
        print("Thanks for game, bye <3")
        break



    if continue_ask not in ("y","n"):
        print("Choose Yes(y) or No (n)")
        continue


     print("Choose a Rock(r) or Paper(p) or Scissors(s)")


    if user_choice == "r":
        user_choice = "🪨"
        print("You chose: 🪨")

    elif user_choice == "p":
        user_choice = "📄"
        print("You chose: 📄")
    elif user_choice == "s":
        user_choice = "✂️"
        print("You chose: ✂️")

    computer_choice = random.choice(game_value)
    print (f"Computer choice: {computer_choice}")
    if computer_choice == user_choice:
        print("Draw!")
    elif (
            (user_choice == "🪨" and computer_choice == "✂️") or
        (user_choice == "📄" and computer_choice == "🪨") or
        (user_choice == "✂️" and computer_choice == "📄")

    ):
        print("You win!")
    else:
        print("You lose!")


