import json



def write_order_to_dump():
    with open('orders.json', 'w') as f:
        json.dump(write_order_to_dirs(), f, indent=4)

def write_order_to_dirs():
    new_list = ['item', 'quentity', 'price', 'buyer', 'date']
    new_dirs = {}
    for i in new_list:
        write_input = input('Введите ' + i + ': ')
        new_dirs[i] = write_input
    return new_dirs


if __name__ == "__main__":
    write_order_to_dump()


