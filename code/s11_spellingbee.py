# https://www.nytimes.com/puzzles/spelling-bee

# Solve today's spelling bee
# Goal: find all the words that meet the following criteria:
# 1. >= 4 letters
# 2. the word has to contain a given letter
# 3. the word must only use the given letters


def at_least(word, n):
    """Return True if word is longer than or equal to n letters"""
    # if len(word) >= n:
    #     return True
    # else:
    #     return False
    return len(word) >= n


# print(at_least('Babson', 4)) # True
# print(at_least('abc', 4)) # False


def must_contain(word, letter):
    """Return True if word contains the letter"""
    # for c in word:
    #     if c == letter:
    #         return True
    # return False
    return letter in word


# print(must_contain('babson', 'f')) # False
# print(must_contain('franklin', 'f')) # True
# print(must_contain('coffin', 'f')) # True


def only_use(word, letters):
    """Return True if word only uses the given letters"""
    for c in word:
        if c not in letters:
            return False
    return True


# print(only_use('babson', 'iaocntf')) # False
# print(only_use('fan', 'iaocntf'))  # True
# print(only_use('ciao', 'iaocntf'))  # True


def solve_spellingbee(center_letter, given_letters):
    """
    Given must have letter and 6 other letters, print all the words that meet the criteria

    Loop over the list of words, check whether the word meets all the criteria, if so, print it
    """
    f = open("data/words.txt")  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if (
            at_least(word, 4)
            and must_contain(word, center_letter)
            and only_use(word, given_letters + center_letter)
        ):
            print(word)


def main():
    required = "f"
    available = "iaocnt"
    solve_spellingbee(required, available)  # it prints all the answers


main()
