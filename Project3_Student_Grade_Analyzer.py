#STUDENT GRADE ANALYZER
print("=== STUDENT GRADE ANALYZER ===")

marks=[]

for i in range(5):
    mark=int(input(f"Enter marks for subject {i+1}:"))
    marks.append(mark)
print("\nMarks list:",marks)  

#Calculate Average, Highest, and Lowest Marks
print("\n==Calculate Average, Highest, and Lowest Marks==")
average=sum(marks)/len(marks)
highest=max(marks)
lowest=min(marks)

print("\nAverage Marks:",average)
print("Highest Marks:",highest)
print("Smallest Marks:",lowest)

#Grade System.
print("\n==Grade System==")
if average>=90:
    Grade="A"
elif average>=75:
    Grade="B"
elif average>=50:
    Grade="C"
else:
    Grade="Fail"
    
print("\nGrade:",Grade)

#performance
print("\n===performance===")

if Grade=="A":
    print("Excellent Performance! 🎉")
elif Grade=="B":
    print("Good Job! 👍")
elif Grade=="C":
    print("Need More Practice 📚")
else:
    print("Work Hard Next Time 💪")

