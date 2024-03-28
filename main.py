from node import Node
import balance
import utils
import timeit
import sys

sys.setrecursionlimit(100000)

loop = True
while loop:

    T = []
    tree = None

    # Zapytanie o wprowadzenie danych
    utils.menu("Jak chcesz wprowadzić dane? ", ["Z klawiatury", "Generator danych losowych"])
    inputType = int(input("Podaj typ wprowadzenia danych: "))

    if inputType == 1:
        print("Podaj ciąg (1 2 3 ...): ", end="")
        T = list(map(int, input().split()))
    elif inputType == 2:
        n = int(input("Podaj długość ciągu: "))
        T = utils.generate_decreasing_sequence(n)
        print(T)

    # Zapytanie o typ drzewa
    utils.menu("Wybierz typ drzewa z listy poniżej", ["Drzewo AVL", "Losowe drzewo BST"])
    treeType = int(input("Podaj typ drzewa: "))

    create_time = 0

    if treeType == 1:
        T.sort()
        tree = utils.createAVL(T)
    elif treeType == 2:
        t0 = timeit.default_timer()
        tree = utils.createRandomBST(T)
        t1 = timeit.default_timer()
        create_time = t1 - t0

    print("---------------")
    print("Twoje drzewo: ")
    tree.printTree()
    print()
    print('Czas tworzenia: {:.6f}s'.format(create_time))

    # Zapytanie o operację
    utils.menu("Wybierz operację z listy poniżej", [
        "Wyszukanie w drzewie MIN i MAX",
        "Wyszukanie poziomu węzła, wypisanie elementów, usuwanie",
        "Wypisanie elementów w porządku malejącym",
        "Wypisanie pre-order oraz własności poddrzewa",
        "Równoważenie drzewa przez rotacje"
    ])
    operationType = int(input("Podaj typ operacji: "))

    if operationType == 1:
        print("MAX: ", end="")
        tree.findMax()
        print("MIN: ", end="")
        t0 = timeit.default_timer()
        tree.findMin()
        t1 = timeit.default_timer()
        print('time =  {:.6f}s'.format(t1 - t0))
    elif operationType == 2:
        key = int(input("Podaj klucz: "))
        level = tree.findLevel(key)
        print(f'Klucz {key} znajduje się na poziomie {level}.')
        print(f'Elementy na poziomie {level}: ', end="")
        tree.printLevel(level)
        tree.deleteNode(key)
        print()
        tree.printTree()
    elif operationType == 3:
        tree.printDescending()
    elif operationType == 4:
        key = int(input("Podaj klucz: "))
        node = tree.getNodeByData(key)
        print(f'Wysokość wybranego poddrzewa = {node.getHeight()}')
        tree.deleteSubtree(key)
        print()
        tree.printTree()
    elif operationType == 5:
        tree.printPreOrder()
        print()
        t0 = timeit.default_timer()
        tree = balance.balanceBST(tree)
        t1 = timeit.default_timer()
        tree.printPreOrder()
        print()
        print('Czas sortowania: {:.6f}s'.format(t1 - t0))

    # Zapytanie o kontynuowanie
    print()
    print("-----------")
    nextRun = input("Czy chcesz kontynuować? Wpisz \"Y\", jeżeli tak: ")
    if nextRun != 'Y':
        loop = False
