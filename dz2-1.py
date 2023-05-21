import csv
import re


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    file_names = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for file_name in file_names:
        with open(file_name, 'r') as file:
            data = file.read()

            os_prod = re.findall(r'Изготовитель системы:\s+(.*)', data)
            os_name = re.findall(r'Название ОС:\s+(.*)', data)
            os_code = re.findall(r'Код продукта:\s+(.*)', data)
            os_type = re.findall(r'Тип системы:\s+(.*)', data)

            if os_prod:
                os_prod_list.append(os_prod[0])
            if os_name:
                os_name_list.append(os_name[0])
            if os_code:
                os_code_list.append(os_code[0])
            if os_type:
                os_type_list.append(os_type[0])

    main_data.extend(zip(os_prod_list, os_name_list, os_code_list, os_type_list))

    return main_data


def write_to_csv(file_path):
    data = get_data()

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


write_to_csv('report.csv')
