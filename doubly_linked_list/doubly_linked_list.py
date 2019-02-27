"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # wrap the input value in a new node
        new_node = ListNode(value)
        # check to see if we have anything in our dll
        # check to see if both head and tail are none
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        # default of new_node next and prev are already set to None, no need to alter
        # if head exists, set self.head.prev to new node
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            # move head to point to new node
            self.head = new_node

    def remove_from_head(self):
        # if dll is empty return none
        # check to see if we have anything in our dll
        # check to see if both head and tail are none
        if self.head == None and self.tail == None:
            return None
        # if head exists return value
        if self.head:
            self.head.delete()
            return self.head.value

    def add_to_tail(self, value):
            # wrap the input value in a new node
        new_node = ListNode(value)
        # check to see if we have anything in our dll
        # check to see if both the head and tail are none
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        # default of new_node next and prev are already set to None, no need to alter
        # if tail exists, set self.tail.next to new node
        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
            # move tail to point to new node
            self.tail = new_node

    def remove_from_tail(self):
        # if dll is empty return none
        # check to see if we have anything in our dll
        # check to see if both head and tail are none
        if self.head == None and self.tail == None:
            return None
        # if tail exists return value
        if self.tail:
            self.tail.delete()
            return self.tail.value

    def move_to_front(self, node):
        # if dll is empty return none
        if self.head == None and self.tail == None:
            return None
        # if node input does not exist return none
        if not node:
            return None
        # if node exists, instantiate, current node
        # change the pointers of the node.next and node.prev
        current_node = node
        if current_node.next:
            current_node.next.prev = current_node.prev
        #
        current_node.prev.next = current_node.next
        if not current_node.prev.prev:
            current_node.prev.prev = current_node.value
        current_node.insert_before(self.head)
        current_node.next = self.head.next.value
        self.head = current_node
        # self.head.next = node.prev.value

    def move_to_end(self, node):
        # if dll is empty return none
        if self.head == None and self.tail == None:
            return None
        # if node input does not exist return none
        if not node:
            return None
        # if node exists, instantiate, current nodes
        # change the pointers of the node.prev and node.next
        current_node = node
        if current_node.prev:
            current_node.prev.next = current_node.next
        #
        current_node.next.prev = current_node.prev
        if not current_node.next.next:
            current_node.next.next = current_node.value
        current_node.insert_after(self.tail)
        current_node.prev = self.tail.prev.value
        self.tail = current_node

    def delete(self, node):
        # if dll is empty return none
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # instantiate current node
        # check if the given node is the head,
        if self.head == node:
            # set the self.head pointer to the next node, delete node
        self.head == node.next
        node.delete()
        # check if the given node is the tail
        if self.tail == node:
            # set the self.tail pointer to the previous node, delete node
        self.tail = node.prev
        node.delete()
        # otherwise, the node we are looking to delete is in the middle of list
        # call node.delete
        else:
            node.delete()

    def get_max(self):
        if self.head == None:
            return None
        current_node = self.head
        max_val = current_node.value
        while current_node is not None:
            if max_val < current_node.value:
                max_val = current_node.value
            current_node = current_node.next
        return max_val


dll = DoublyLinkedList()
dll.remove_from_head()
dll.add_to_head(5)
# dll.add_to_head(6)
# dll.add_to_head(7)
print(dll.head.value)
print(dll.tail.value)
print(dll.remove_from_head())
