# A hash table lookup is performed in constant time - O(1)
book = {}
book['apple'] = 0.67
book['avocado'] = 1.49
print(book)
print(book['avocado'])
print(book.get('apple'))
