word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'

encoded_word1 = word1.encode()
encoded_word2 = word2.encode()
encoded_word3 = word3.encode()

decoded_word1 = encoded_word1.decode()
decoded_word2 = encoded_word2.decode()
decoded_word3 = encoded_word3.decode()

print(type(encoded_word1), encoded_word1)
print(type(encoded_word2), encoded_word2)
print(type(encoded_word3), encoded_word3)

print(type(decoded_word1), decoded_word1)
print(type(decoded_word2), decoded_word2)
print(type(decoded_word3), decoded_word3)
