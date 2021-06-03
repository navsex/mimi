import os
import csv


def file(path):
    return [f for f in os.listdir(path) if f.endswith('.txt')]

def data():
    data_list = []
    for i in list1:
        with open(i) as f:
            for l in f:
                data_list.append([l])
    return data_list

def file_csv():
    with open('info.csv', 'w') as f:
        f_writer = csv.writer(f)
        for a in data():
            f_writer.writerow(a)


def file_csv_online():          # можно не делать сделал для вывода
    with open('info.csv') as f_online:
        return f_online.read()


if __name__ == "__main__":

    list1 = file('/mimi/1')

    print(list1)            # сделанно для нагдяжности
    print(data())           # сделанно для нагдяжности
    print(file_csv_online())# сделанно для нагдяжности
