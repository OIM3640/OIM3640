# https://www.nytimes.com/puzzles/spelling-bee


def at_least(word, n):
    """return True if the length of word >= n"""
    return len(word) >= n


def must_use(word, required):
    """
    Return True if the word uses the required letter, False otherwise
    """
    # if required in word:
    #     return True
    # else:
    #     return False
    return required in word


# print(must_use('babson', 'b'))
# print(must_use('babson', 'c'))


def use_only(word, available):
    """
    Return True if the word only use the available letters, return False if the word uses any letter outside the give available letters
    """
    for letter in word:
        if letter not in available:
            return False

    return True


def solve_spelling_bee(required, available, n):
    """
    Given a required letter and several available letters, print all the possible words

    Return the word list

    idea: iterate over word list, find the words that satisfy the requirements (must use the required letter, and must not use any letters outside available letters)
    """
    f = open("data/words.txt")
    words = []

    for line in f:
        word = line.strip()
        if (
            at_least(word, n)
            and must_use(word, required)
            and use_only(word, available + required)
        ):
            # print(word)
            words.append(word)
    return words


def main():
    required = "v"
    available = "itaecl"
    num_letters = 4
    results = solve_spelling_bee(required, available, num_letters)
    print(results)


if __name__ == "__main__":
    main()
