# Поиск в хеш-таблице выполняется за постоянное время.
# O(1)
book = {}
book['apple'] = 0.67
book['avocado'] = 1.49
print(book)
print(book['avocado'])
print(book.get('apple'))
