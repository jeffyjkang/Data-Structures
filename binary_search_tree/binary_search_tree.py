class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # insert inserts a node value into the BST,
    # if there is no root value, must create a root node
    # if there is a root value, must compare inserted node with value
    # if the new node is less than the value insert to left node
    # if the new node is greater than the value insert to right node
    def insert(self, value):
        # check to see if we have anything in our BST
        new_node = Node(value)
        if self.value == None:
            self.value = new_node
            print(self.value)
        # if we have a root value invoke the private recursive function
        else:
            self._insert(value, new_node)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    # create another private recursive function
    def _insert(self, value, current_node):
        print(self.value)
        print(value)
        # check to see if the value is less than the current node's value
        if value < current_node.value:
            # if there is no left child, insert the value in the left node
            # if current_node.left_child == None:
            if self.left == None:
                # current_node.left_child = Node(value)
                self.left = Node(value)
            # if there is a left child, recursively call _insert
            else:
                # self._insert(value, current_node.left_child)
                self._insert(value, self.left)
        # if value is not less than current node's value, move to right side
        if value > current_node.value:
            # if there is no right child, insert the value in the right node
            # if current_node.right_child == None:
            if self.right == None:
                # current_node.right_child = Node(value)
                self.right = Node(value)
            # if there is a right child, recursively call _insert again but on the right
            else:
                # self._insert(value, current_node.right_child)
                self._insert(value, self.right)
        # if value is already in tree, error out with a string
        else:
            print("value already in BST")

    # def print_tree(self):
    #     if self.value != None:
    #         self._print_tree(self.value)

    # def _print_tree(self, current_node):
    #     if current_node != None:
    #         # self._print_tree(current_node.left_child)
    #         self._print_tree(current_node.left)
    #         print(f"{current_node.value}")
    #         # self._print_tree(current_node.right_child)
    #         self._print_tree(current_node.right)


class Node:
    def __init__(self, value=None):
        self.value = value
        # self.left_child = None
        # self.right_child = None

    def get_value(self):
        return self.value


# def fill_tree(tree, elem=10, max_int=100):
#     from random import randint
#     for i in range(elem):
#         cur_elem = randint(0, max_int)
#         tree.insert(cur_elem)
#         return tree


tree = BinarySearchTree()
# tree = fill_tree(tree)
tree.insert(5)
tree.insert(6)
# tree.print_tree()
print(tree)


# should have methods insert, contains, get_max
# insert adds the input value to the tree, adhering to the rules of the ordering of elements in a binary search tree
# contains searches the binary search tree for the input value returning a bool indicating whether the value exists in the tree or not
# get_max returns the max value in the tree

# binary search tree, have a root node
# elements that are less than the root/ parent node will be inserted on the left
# elements that are greater than the root/ parent node will be inserted on the right
# elements that have no child nodes are "leaf nodes"

# full binary tree, all leaf nodes are at same level and filled
# complete binary tree, all levels of tree are full except last, all nodes are left as possible
# balanced binary tree, all leaves are not too far in difference in depth
# unbalanced binary tree, does not meet three conditions
