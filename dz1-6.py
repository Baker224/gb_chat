import chardet

with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write('сетевое программирование\n')
    file.write('сокет\n')
    file.write('декоратор\n')

with open('test_file.txt', 'rb') as file:
    content = file.read()
    result = chardet.detect(content)
    encoding = result['encoding']

print(f"Кодировка файла по умолчанию: {encoding}")

with open('test_file.txt', 'r', encoding=encoding) as file:
    content = file.read()

print(content)
