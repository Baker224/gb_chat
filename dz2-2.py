import json


def write_order_to_json(item, quantity, price, buyer, date):
    order_data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'w') as file:
        json.dump(order_data, file, indent=4)


write_order_to_json('Телефон', 1, 1000, 'Иванов', '2023-03-29')
