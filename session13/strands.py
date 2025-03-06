# Solve Strands Game https://www.nytimes.com/games/strands

puzzle = ["SWIPEP", "PROMTU", "ELIFEE"]
# Choosing a better data structure, list

print(len(puzzle))
print(len(puzzle[0]))

row, col = 0, 0

current = puzzle[row][col]
print(current)

row += 1
current = puzzle[row][col]
print(current)

"""
# How to Create a strands puzzle
# Constraints/thoughts
1. find a theme, which defines a subset of words
2. total number of letters = 48

Suppose we have 5 words that sum up to 44 letters, what word has lenght of 4?

"""