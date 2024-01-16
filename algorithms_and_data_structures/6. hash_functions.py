# A hash table lookup is performed in constant time - O(1)
# book = {}
# book['apple'] = 0.67
# book['avocado'] = 1.49
# print(book)
# print(book['avocado'])
# print(book.get('apple'))

# dict is hash table data structure
d = {'one': 1,
     'two': 2,
     'five': 5,
     }
d['three'] = 3
# print(d)

value = d['one']
# print(value)

# you should only use hashable objects for Python keys.
# Рashable objects are objects with immutable data type - str, tuple, bool, int, float.

# try:
#     k = [1,2,3]
#     d[k] = 123
# except TypeError:
#     print(f"Unhashable key: '{k}'.")


# set - implemented based on hash tables
s = {'one', 'two', 'three'} # difference from dict - set contains only keys without values
print(s)
# set should contain only hashable types
try:
    s = {'one', 'two', 'three', [1,2,3]}
except:
    print('Unhashable type of data in your set.')
print(s)
