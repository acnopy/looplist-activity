x = 0
wordlist = []
while x < 1:
    y = 0
    word = input("Enter a word: ")
    wordlist.append(word)
    counter = len(wordlist)
    print("Your current words are:", wordlist)
    while y < 1:
        try_again = input("Would you like to try again? (y/n): ").lower()
        if try_again == "y":
            y += 1
        elif try_again == "n":
            print("The total number of words are:", counter)
            print("The words are:")
            for wor in wordlist:
                print(wor, end=" ")
            x += 1
            break
        else:
            print("Invalid input")
