#Password generator

import random

while True:
    print("===PASSWORD GENERATOR===")

    print("\nChoose password type")
    print("1. Numbers only")
    print("2. Letters only")
    print("3. Strong password")

    choice=int(input("\nEnter your choice:"))

    if choice==1:
        character="0123456789"
    elif choice==2:
        character="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif choice==3:
        character="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    else:
        print("Invalid choice!")
        exit()
    
    
    length=int(input("\nEnter password length:"))

    password=""

    for i in range(length):
        password+=random.choice(character)
    
    print("\nGenerated Password:")
    print(password)


    again=input("\nGenerate another password?(Y/N): ")
    
    if again.lower() != "y":
        print("\n==Thankyou🙏==")
        break