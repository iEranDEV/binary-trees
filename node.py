class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Dodanie elementu do drzewa (automatycznie szuka miejsca i wstawia)
    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            return self

    # Zwraca Node zależnie od podanej wartości
    def getNodeByData(self, data):
        if data < self.data and self.left:
            return self.left.getNodeByData(data)
        elif data > self.data and self.right:
            return self.right.getNodeByData(data)
        elif data == self.data:
            return self
        return None

    # Szukanie najmniejszej wartości w drzewie
    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data

    # Szukanie największej wartości w drzewie
    def findMax(self):
        if self.right:
            return self.right.findMax()
        return self.data

    # Wypisanie wszystkich elementów drzewa w porzadku malejącym
    def printDescending(self):
        if self.right:
            self.right.printDescending()
        print(self.data)
        if self.left:
            self.left.printDescending()

    # Zwraca wysokość drzewa
    def getHeight(self):
        leftHeight = self.left.getHeight() if self.left else 0
        rightHeight = self.right.getHeight() if self.right else 0
        return max(leftHeight, rightHeight) + 1

    # Wypisz poziom, na którym znajduje się dany element
    def findLevel(self, data, level=0):
        if data > self.data and self.right:
            return self.right.findLevel(data, level + 1)
        elif data < self.data and self.left:
            return self.left.findLevel(data, level + 1)
        else:
            return level
