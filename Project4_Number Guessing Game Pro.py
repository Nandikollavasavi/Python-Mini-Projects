#Number Guessing Game Pro
import random

print("===Number Guessing Game===")
print("\n Choose Difficulty")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-200)")

level=int(input("\nEnter your level:"))

if level==1:
    number=random.randint(1,50)
elif level==2:
    number=random.randint(1,100)
elif level==3:
    number=random.randint(1,200)
else:
    print("Invalid Choice!!")
    exit()
    
if level == 1:
    max_attempts = 5
elif level == 2:
    max_attempts = 7
else:
    max_attempts = 10
    
attempts=0

while attempts<max_attempts:
    guess=int(input("\nEnter your number:"))
    attempts+=1
    
    if attempts==max_attempts and guess!=number:
        print("\n❌ Game Over!")
        print("The correct number was:", number)
        
    elif attempts<=max_attempts and guess==number:
        print("\n🎉Congratulations!")
        print("You guessed the number in",attempts,"attempts.")
        break
    elif guess>number:
        print("\nToo High! ⬆️")
        
    else:
        print("\nToo Low! ⬇️")