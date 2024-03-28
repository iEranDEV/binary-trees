import random
from node import Node


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


def generate_decreasing_sequence(size):
    temp = random.sample(range(1, size * 10), size)
    temp.sort()
    return temp[::-1]


def createRandomBST(array):
    temp = Node(array[0])
    for i in range(1, len(array)):
        temp.insert(i)
    return temp


def createAVL(arr):
    if not arr:
        return None
    mid = (len(arr) - 1) // 2
    root = Node(arr[mid])
    root.left = createAVL(arr[:mid])
    root.right = createAVL(arr[mid + 1:])
    return root
