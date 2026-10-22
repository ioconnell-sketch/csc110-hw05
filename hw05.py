"""
Name: Issy O'Connell
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """Ask for a single letter (A, B, or C) and keep asking until it is valid."""
    while True:
        text = input("Give an single uppercase letter: ")
        # Check the length first
        if len(text) != 1:
            print("Error: it needs to be a single character.")
            continue
        # Then check that it is one of the allowed letters
        if text != "A" and text != "B" and text != "C":
            print("Error: You provided the wrong character.")
            continue
        return text

def get_digit():
    """Ask for a single digit (1, 2, or 3) and keep asking until it is valid."""
    while True:
        text = input("Give an single number character: ")
        # Must be digits only
        if not text.isdigit():
            print("Error: your input should be only digits.")
            continue
        # Must be 1, 2, or 3
        if text != "1" and text != "2" and text != "3":
            print("Error: a single digit needs to be in [1,3].")
            continue
        return text


def check_pattern(letter, digit, lst):
    """Print every word where letter appears before digit."""
    print("Strings with the pattern:")
    for word in lst:
        found = False
        # Find the letter, then look for the digit after it
        for i in range(len(word)):
            if word[i] == letter:
                for j in range(i + 1, len(word)):
                    if word[j] == digit:
                        found = True
        # Print each matching word once, on the same line
        if found:
            print(word, end=" ")
    print()


def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        again = input("Try Again? (y/n): ")
        if again != "y":
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")


# Do not modify these two lines
if __name__ == "__main__":
    main()