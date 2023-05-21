words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        word.encode('ascii')
        print(f"Можно записать слово '{word}' в байтовом типе")
    except UnicodeEncodeError:
        print(f"Невозможно записать слово '{word}' в байтовом типе")
