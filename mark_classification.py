def calculate_grade(mark):
    """Calculate the grade based on the mark."""
    if mark < 50:
        return "Fail"
    elif mark < 70:
        return "Credit"
    else:
        return "Distinction"


def main():
    print("=== Student Mark Grading System ===")
    print("Enter a negative number to exit.\n")

    while True:
        try:
            mark = int(input("Enter mark (0-100): "))

            if mark < 0:
                break

            if mark > 100:
                print("Invalid mark. Please enter a value between 0 and 100.\n")
                continue

            grade = calculate_grade(mark)
            print(f"Result: {grade}\n")

        except ValueError:
            print("Error: Please enter a whole number.\n")


main()

print("Thanks. See you next time.")
