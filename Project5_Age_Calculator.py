#Age Calculator

from datetime import date 

today=date.today()
print("Today's Date:",today)

print("\n=== AGE CALCULATOR ===")

birth_year=int(input("\nEnter your birth year:"))
birth_month=int(input("Enter your birth month:"))
birth_day=int(input("Enter your birth day:"))

birth_date=date(birth_year, birth_month, birth_day)
print("\nBirth date:",birth_date)

#Age

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("\n=== AGE DETAILS ===")
print("\nYour Age is:", age, "years")

if today.month==birth_date.month and today.day==birth_date.day:
    print("🎉Happy Birthday!🎂")
else:
    print("Have a wonderful day!😊")