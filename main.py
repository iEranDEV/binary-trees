from node import Node
import utils


def createRandomBST(array):
    temp = Node(array[0])
    for i in range(1, len(array)):
        temp.insert(array[i])
    return temp


def createAVL(array):
    # TODO: Funkcja na konstruowanie drzewa AVL metodą przeszukiwania binarnego
    return 1


loop = True
while loop:

    # Debug
    T = [8, 2, 5, 14, 1, 10, 12, 13, 6, 9]
    tree = createRandomBST(T)

    # Zapytanie o typ drzewa
    utils.menu("Wybierz typ drzewa z listy poniżej", ["Drzewo AVL", "Losowe drzewo BST"])
    treeType = int(input("Podaj typ drzewa: "))

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
        tree.findMin()
    elif operationType == 2:
        key = int(input("Podaj klucz: "))
        level = tree.findLevel(key)
        print(f'Klucz {key} znajduje się na poziomie {level}.')
        print(f'Elementy na poziomie {level}: ', end="")
        tree.printLevel(level)
        # TODO: Usunięcie tego węzła
    elif operationType == 3:
        tree.printDescending()
    elif operationType == 4:
        key = int(input("Podaj klucz: "))
        node = tree.getNodeByData(key)
        print(f'Wysokość wybranego poddrzewa = {node.getHeight()}')
        # TODO: Usunięcie tego poddrzewa metodą post-order
    elif operationType == 5:
        # TODO: Równoważenie drzewa przez rotacje
        print()

    # Zapytanie o kontynuowanie
    print()
    print("-----------")
    nextRun = input("Czy chcesz kontynuować? Wpisz \"Y\", jeżeli tak: ")
    if nextRun != 'Y':
        loop = False
