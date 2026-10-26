try:
    number = input("Enter a positive integer: ")

    if not number.isdigit():
        print("Please enter a positive integer.")
    else:
        largest = max(number)
        print("Largest digit:", largest)

except ValueError:
    print("Invalid input!")