import yaml

data = {
    'list': ['item1', 'item2', 'item3'],
    'number': 42,
    'nested_dict': {
        'key1': 'value1',
        'key2': 'value2',
        'key3': '€'
    }
}


with open('file.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


with open('file.yaml', 'r') as file:
    loaded_data = yaml.load(file, Loader=yaml.FullLoader)

print(loaded_data == data)
