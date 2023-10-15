i = 0
while i < 1:
    n = 0
    n1 = int(input("Enter the first integer: "))
    n2 = int(input("Enter the second integer: "))
    total = n1 + n2
    print("The sum of", n1, "and", n2, "is", total)
    while n < 1:
        try_again = input("Would you like to try again? (y/n): ").lower()
        if try_again == "y":
            n += 1
        elif try_again == "n":
            print("Thank you!")
            i += 1
            break
        else:
            print("Invalid input")
