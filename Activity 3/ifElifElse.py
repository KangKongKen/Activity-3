score = int(input("Enter your quiz score (0-100): "))

if score >= 90:
    print("Excellent! You got an A.")
elif score >= 75:
    print("Good job! You got a B.")
elif score >= 60:
    print("You passed with a C.")
else:
    print("You failed. Better luck next time.")
