class Node:
    def __init__(self, data=None):
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
    def findMin(self, write=True):
        if self.left:
            if write:
                print(f'{self.data} -> ', end="")
            return self.left.findMin(write)
        if write:
            print(self.data)
        return self.data

    # Szukanie największej wartości w drzewie
    def findMax(self, write=True):
        if self.right:
            if write:
                print(f'{self.data} -> ', end="")
            return self.right.findMax(write)
        if write:
            print(self.data)
        return self.data

    # Wypisanie wszystkich elementów drzewa w porzadku malejącym
    def printDescending(self):
        if self.right:
            self.right.printDescending()
        print(self.data, end=" ")
        if self.left:
            self.left.printDescending()

    # Wypisanie drzewa
    def printTree(self, level=0):
        print(f'{level * "    "} {self.data}')
        if self.left:
            self.left.printTree(level + 1)
        if self.right:
            self.right.printTree(level + 1)

    # Wypisanie elementów drzewa w porządku pre-order
    def printPreOrder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()

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

    # Wypisanie elementów na poziomie LEVEL
    def printLevel(self, level, currLevel=0):
        if currLevel == level:
            print(self.data, end=" ")
        else:
            if self.left:
                self.left.printLevel(level, currLevel + 1)
            if self.right:
                self.right.printLevel(level, currLevel + 1)

    # Usunięcie węzła z drzewa
    def deleteNode(self, data):
        if self is None:
            return self
        if data < self.data:
            self.left = self.left.deleteNode(data)
            return self
        if data > self.data:
            self.right = self.right.deleteNode(data)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.data = min_larger_node.data
        self.right = self.right.deleteNode(min_larger_node.data)
        return self

    def deleteSubtree(self, data):
        parent = None
        current = self
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if not current:
            return
        if parent:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        else:
            self.data = None
            self.left = None
            self.right = None
        self.deleteSubtreeUtil(current.left)
        self.deleteSubtreeUtil(current.right)

    def deleteSubtreeUtil(self, node):
        if not node:
            return
        self.deleteSubtreeUtil(node.left)
        self.deleteSubtreeUtil(node.right)
        node.data = None
        node.left = None
        node.right = None


