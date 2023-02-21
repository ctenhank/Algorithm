class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node = None
        self.right: Node = None


class BinarySearchTree:
    def __init__(self):
        self._root: Node = None

    def search(self, value):
        if self._root == None:
            return None

        cur = self._root
        

    def insert(self, value):
        if self._root == None:
            self._root = Node(value)
            return

        cur = self._root
        while True:
            if value < cur.value:
                if cur.left == None:
                    cur.left = Node(value)
                    break
                else:
                    cur = cur.left
            elif value > cur.value:
                if cur.right == None:
                    cur.right = Node(value)
                    break
                else:
                    cur = cur.right


bst = BinarySearchTree()
bst.insert(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
