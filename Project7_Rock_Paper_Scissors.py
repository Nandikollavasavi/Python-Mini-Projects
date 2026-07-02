#_Rock_Paper_Scissors

your_Score=0
computer_score=0

while True:
    import random
    print("\n=== ROCK PAPER SCISSORS ===")
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice=["Rock","Paper","Scissors"]

    user_choose=int(input("\nEnter your choice:"))

    if user_choose==1:
        user_choice="Rock"
    elif user_choose==2:
        user_choice="Paper"
    elif user_choose==3:
        user_choice="Scissors"
    else:
        print("Invalid choice!")
        exit()

    print("\nyou Choose:",user_choice)

    computer_choose=random.choice(choice)
    print("Computer choose:",computer_choose)

    if user_choice==computer_choose:
        print("\n==It's a tie🤝==")
    elif (user_choice=="Rock" and computer_choose=="Scissors") or (user_choice=="Paper" and computer_choose=="Rock") or (user_choice=="Scissors" and computer_choose=="Paper"):
        print("\n🎉You Win")
        your_Score+=1
    else:
        print("\n🖥️Computer Win")
        computer_score+=1
    
    print("\n==Score==")
    print("Your Score:",your_Score)   
    print("Computer Score:",computer_score) 
    
    play_again=input("\nDo you want play again? (yes/no):").lower()
    if play_again != "yes":
        print("\nFinal Score:",your_Score)
        print(f"You:{your_Score} | computer:{computer_score}")
        print("Thanks for playing!!")
        break