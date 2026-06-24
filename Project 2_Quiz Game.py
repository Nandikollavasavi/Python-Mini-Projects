print("===PYTHON QUIZ GAME===")

questions={
    "(1) Which of the following is a valid variable name?\na) 1name\nb) my-name\nc) my_name\nd) class":"c",
    "(2) What is the output?\nprint\na) int\nb) float\nc) string\nd) bool":"a",
    "(3) What is the keyword for creating function in python?\na) func\nb) define\nc) def\nd) function":"c",
    "(4) Which symbol is used for comments in Python?\na) //\nb) #\nc) /*\nd) --":"b",
    "(5) Which data type is used to store True or False values?\na) int\nb) bool\nc) float\nd) string":"b",
    "(6) Which function is used to get input from the user?\na) input()\nb) read()\nc) get()\nd) print()":"a",
    "(7) Which data structure stores multiple items in a single variable and uses square brackets []?\na) Tuple\nb) Dictionary\nc) List\nd) Set":"c",
    "(8) Which operator is used for exponentiation (power)?\na) **\nb) *\nc) //\nd) ^":"a",
    "(9) Which keyword is used to create a loop?\na) repeat\nb) loop\nc) for\nd) iterate":"c",
    "(10) Which data type is immutable?\na) List\nb) Dictionary\nc) Set\nd) Tuple":"d"
}

score=0
for question in questions:
    print("\n"+question)
    
    answer=input("\nEnter your answer:")
    
    if answer.lower()==questions[question]:
        print("\nCorrect!")
        score+=1
    else:
        print("\nWrong!!")
        
print("\n=== QUIZ COMPLETED ===")
print("Final score:",score,"/",len(questions))

if score==len(questions):
    print("\nExcellent🎉")
elif score>=len(questions)//2:
    print("\nGood Job👍")
else:
    print("\nPlay again🙃")