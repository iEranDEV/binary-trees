import random


def menu(title, options):
    print("-----------")
    print(title)
    for index, option in enumerate(options):
        print(f'  [{index + 1}.] {option}')
    print("-----------")


def generate(size):
    values = []
    for i in range(size):
        values.append(random.randint(1, size * 10))
    return values
