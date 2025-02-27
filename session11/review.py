# How do we check if a string contains any vowel letter ('a', 'e', 'i', 'o', 'u')?

def contain_vowel(s):
    """
    Do not use any() 
    """
    vowels = 'aeiou'
    for letter in s.lower():
        if letter in vowels:
            return True
    
    
    
    return False # return immediately ends the function


print(contain_vowel('abc')) # True
print(contain_vowel('Babson')) # True
print(contain_vowel('bcd')) # False