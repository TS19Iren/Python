# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
words = 'самозаБвенно мне была не понятна абвиотура'
words = words.lower()
words = words.split(' ')
elem = 'абв'
new_string = []
for word in words:
    if elem not in word:
        new_string.append(word)
print(new_string)
