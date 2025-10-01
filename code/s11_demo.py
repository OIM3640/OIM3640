def any_vowel_6(s):
    for c in s:
        if c in 'aeiouAEIOU':
            return True
            break
    return False

print(any_vowel_6('aaeeeoo'))
print(any_vowel_6('HTML'))