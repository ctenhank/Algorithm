class Node:
    def __init__(self, depth, value=None):
        self._value = value
        self._depth = depth
        self._dummy = False
        if value is None: 
            self._dummy = True

        self.left = None
        self.right = None
    
    @property
    def depth(self):
        return self._depth
    @property
    def value(self):
        return self._value
    @property
    def dummy(self):
        return self._dummy


class BinaryTree:
    def __init__(self):
        self._root = None
        self._height = 0
        self._length = 0

    @property
    def root(self):
        return self._root

    @property
    def height(self):
        return self._height

    @property
    def length(self):
        return self._length

    def is_duplicated(self, value):
        cur = self._root
        while cur:
            if cur.value == value:
                return True
            elif cur.value > value:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def insert(self, value):
        if self._root is None:
            self._root = Node(value=value, depth=1)
            self._length += 1
            return
            
        if self.is_duplicated(value):
            # print(f'Duplicated value: {value}')
            return

        cur = self._root
        height = self._root.depth

        while cur:
            height += 1

            if cur.value < value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(value=value, depth=height)
                    self._length += 1
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(value=value, depth=height)
                    self._length += 1
                    break

        self._height = max(self._height, height)

    def make_full_binary_tree(self):
        self._make_full_binary_tree(self._root)
    
    def _make_full_binary_tree(self, node):
        if node.depth == self._height:
            return
        
        if node.left is None:
            node.left = Node(value=None, depth=node.depth+1)
            self._length += 1
        if node.right is None:
            node.right = Node(value=None, depth=node.depth+1)
            self._length += 1
        
        self._make_full_binary_tree(node.left)
        self._make_full_binary_tree(node.right)

    def _get_bin(self, node):
        if node.dummy:
            return '0'
        return '1'

    def binary_tree_to_binary_value(self):
        return self._binary_tree_to_binary_value(self._root)

    def _binary_tree_to_binary_value(self, node):
        if node is None:
            return ''

        return self._binary_tree_to_binary_value(node.left) + \
         self._get_bin(node) + \
         self._binary_tree_to_binary_value(node.right)

def binary_to_decimal(binary):
    pass


def get_fbt_size(num_node):
    n = 1
    while True:
        if 2**(n-1) -1 < num_node and \
           2 **(n) -1 >= num_node:
           return 2 ** n -1
        n += 1

def decimal_to_binary(num):
    return bin(num).replace('0b', '')

def solve(num):
    binary = decimal_to_binary(num)
    # 먼저 Full BT로 변경해야 하는데 만약 이진수가 FBT가 아닐 때 앞자리에 0을 채워넣어야 함
    fbt_size = get_fbt_size(len(binary))
    fbt_binary = '0' * (fbt_size - len(binary)) + binary

    # 리프 노드가 dummy가 아닌데 중간 노드가 dummy인 경우
    
    print(fbt_binary)

    return 0



def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(solve(num))

    return answer

s = 'asdfasdfas'
