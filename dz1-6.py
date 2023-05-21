import chardet


with open('test_file.txt', 'wb') as file:
    content = 'сетевое программирование\nсокет\nдекоратор\n'
    file.write(content.encode())


with open('test_file.txt', 'rb') as file:
    content = file.read()
    result = chardet.detect(content)
    encoding = result['encoding']

print(f"Кодировка файла по умолчанию: {encoding}")


with open('test_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print(content)
