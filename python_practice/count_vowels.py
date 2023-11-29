def count_vowels(string):
    res = 0
    vowels = 'AEIOUYaeiouy'
    for i in string:
        if i in vowels:
            res += 1
    return res
