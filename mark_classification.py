while True:
    try:
        mark = int(input("Enter mark (0-100; to quit, enter a negative value): "))

        if mark < 0:
            break

        if mark < 50:
            print("Fail")
        elif mark < 70:
            print("Credit")
        elif mark <= 100:
            print("Distinction")
        else:
            print("Invalid mark. Please re-enter.")

    except ValueError:
        print("Error: Please enter numbers only. ")

print("Thanks. See you next time.")