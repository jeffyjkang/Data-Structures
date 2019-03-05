class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # self.storage =
        self.front = None
        self.back = None

    # enque adds an item to the back of the queue
    def enqueue(self, item):
        # wrap the input value into a new node
        # back node defaults to front node
        new_node = Node(item)
        # check to see if we have anything in our que
        # check to see if we have anything in the front of our queue
        # increment the size of the queue by 1
        if not self.front:
            self.front = new_node
            self.back = new_node
            self.size += 1
        # if something is in our queue and we have a node in the front
        # set the new node as the back's next node
        else:
            self.back.set_next(new_node)
            # update the self.back reference accordingly
            self.back = new_node
            self.size += 1

    # dequeue removes item in the front of the queue and returns the value
    def dequeue(self):
        # check to see if we have a queue at all, and return queue is empty if no queue
        if not self.front:
            return None
        # otherwise there is a queue, and we can remove item in front
        # check to see if we only have one element in the queue

        # check to see if self.front == self.back
        if self.front == self.back:
            front = self.front
            self.front = None
            self.back = None
            self.size = 0
            return front.value
        # if we have multiple elements in queue
        else:
            # grab second reference to fron element
            front = self.front
            # reassign self.head reference to current head's next node
            self.front = self.front.get_next()
            self.size -= 1
            return front.value

    def len(self):
        return self.size
        # pass


# enqueue should add an item to the back of the queue
# dequeue should remove and return an item from the front of the queue
# len returns the number of items in the queue

# build the queue data structure
    # first in first out, list
    # a queue is nothing more than a list which is limited to only allow data to be inserted from one end and retrieved from the other
    # for this case i will make a single linked node list, which will only have to worry about the head, tail and next node of each node in the linked node list
    # we can then use the methods enqueue, dequeue and len after modifying the size property whenever enqueue or dequeue is invoked

# first build the Node class
#
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


# newQ = Queue()
# print(newQ.size)
# print(newQ.dequeue())
# newQ.enqueue('5')
# print(newQ.size)
# newQ.enqueue('6')
# print(newQ.size)
# newQ.dequeue()
# print(newQ.size)
