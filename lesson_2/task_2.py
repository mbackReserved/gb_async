import json


def write_order_to_json(**data):
    with open('orders.json', 'r+') as f:
        objs = json.load(f)
        objs['orders'].append(data)
        json.dump(objs, f, indent=4)
    with open('orders.json', 'w') as f:
        json.dump(objs, f, indent=4)
    return objs


if __name__ == "__main__":
    write_order_to_json(item = 'Pen', quantity = 3, price = 2.50, buyer = 'Vadim', date='12 October')
    write_order_to_json(item = 'Bag', quantity = 13, price = 6.50, buyer = 'Alex', date='1 January')