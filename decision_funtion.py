grade = int(input("Enter your grade: "))
if grade < 0 or grade > 100:
    print("Invalid grade")
elif grade >= 90:
    print("Excellent")
elif grade >= 75:
    print("Pass")
else:
    print("Fail")
