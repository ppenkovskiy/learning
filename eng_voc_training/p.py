import random

import openpyxl

# Load the Excel file
workbook = openpyxl.load_workbook('english_words.xlsx')

# Select the worksheet to read from
worksheet = workbook.active

# Create empty dictionaries to store the words and their translations
english_to_russian = {}
russian_to_english = {}

# Read each row in the worksheet and add the word and translation to the dictionaries
for row in worksheet.iter_rows(values_only=True):
    english_word = row[0]
    russian_translation = row[1]
    if english_word is not None and russian_translation is not None:
        english_to_russian[english_word] = russian_translation
        russian_to_english[russian_translation] = english_word

while True:
    etr = english_to_russian
    key = random.choice(list(etr))
    print(key)
    res = input('Your translation is : ')
    if res == etr[key]:
        print('Correct!')
    else:
        print(f'Incorrect... The answer is {etr[key]}')
