prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    # if letter == 'O' or 'Q': # Always True
    if letter == 'O' or letter=='Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)