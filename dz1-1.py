word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'

print(type(word1), word1)
print(type(word2), word2)
print(type(word3), word3)

unicode_word1 = word1.encode('unicode-escape').decode()
unicode_word2 = word2.encode('unicode-escape').decode()
unicode_word3 = word3.encode('unicode-escape').decode()

print(type(unicode_word1), unicode_word1)
print(type(unicode_word2), unicode_word2)
print(type(unicode_word3), unicode_word3)
