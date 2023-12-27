# dict and set in python - in fact are hash-table

# dict - implemented based on hash tables
d = {'one': 1,
     'two': 2,
     'five': 5,
     }
d['three'] = 3
# print(d)

value = d['one']
# print(value)

# you should use only hashable objects for python keys
# hashable objects are objects with immutable data type - str, tuple, bool, int, float

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
