# Prompt the user for their numeric grade
user_input = input("Enter your numeric grade: ")

try:
    # Convert input to an integer
    grade = int(user_input)

    # Determine the letter grade using if...elif...else
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Print the letter grade
    print(f"Your grade is: {letter_grade}")

except ValueError:
    print("Invalid input. Please enter an integer.")