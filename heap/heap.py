class Heap:
    def __init__(self):
        # storage is the list/ array we make to store the value at each index
        # to allow easier math functions when accessing indecies, initialize the
        # 0th index of the storage with 0, we will not be using this place-holder index
        # or the value.
        self.storage = [0]
        # for i in items:
        #     self.storage.append(i)
        #     self._bubble_up(len(self.storage)-1)

    def insert(self, value):
        # on each insert, we are going to append the value to storage, (end of list)
        self.storage.append(value)
        # every time we insert a value, we have to make sure the max value is up top
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        # to delete we have three conditions, when length of storage is 1,
        # which means there is nothing in the heap
        # when length is 2, which means there is one value in the heap
        # and when it is greater than two
        # when length of storage is greater than two, we have to swap the first index
        # which at this point is the greatest value, with the last index in the list
        # after which we store the max_value from the new position which is the last index
        # in the list and then sift the new 1st index which was the last index previously
        # if length of storage is equal to 1, return none, there is nothing to delete
        if len(self.storage) == 1:
            return None
        # if the length of the storage is equal to 2, which would mean 1 value
        # all you need to do is pop the value at the end of the list
        if len(self.storage) == 2:
            max_val = self.storage.pop()
        # if the length of the storage is greater than 2 we need to swap the largest value
        # with the last index of the list
        if len(self.storage) > 2:
            self._swap(1, len(self.storage)-1)
            # after the swap we assign max_val to the last index
            max_val = self.storage.pop()
            # call sift down on index of one, which used to be the last index
            self._sift_down(1)
        # return max value
        return max_val

    def get_max(self):
        # get max checks to see if there is a value at the 1st index, if it does
        # return that value, if not return None
        if self.storage[1]:
            return self.storage[1]
        else:
            return None

    def _swap(self, i, j):
        # all we need to do in the swap function is to swap the 1st index with the last
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def get_size(self):
        # because we initialized the storage with 0 at the 0th index we must be sure
        # to get length of storage -1
        return len(self.storage)-1

    def _bubble_up(self, index):
        # the bubble up function works when we insert a value, when appending
        # the value will be at the last index, we need to compare with parent index
        # and if the parent index value is less, swap and recursively call until it is not
        # there are two possibilities, when the appending value is at index 1,
        # there is no bubbling that is needed, and it is already at the top
        # the parent index will be the floor of index divided by 2
        parent = index // 2
        # if index is 1, dont do anything
        if index <= 1:
            return
        # if value at index is greater than value at parent swap
        if self.storage[index] > self.storage[parent]:
            self._swap(index, parent)
            # recursively call until the if condition is not met
            self._bubble_up(parent)

    def _sift_down(self, index):
        # this function is invoked when using the delete function to return the topmost value
        # we need to define the left child and the right child of the index we are currently at
        # left child will be index times 2
        left = index * 2
        # right child will be index times 2 + 1
        right = index * 2 + 1
        # we must initialize the largest placeholder with the current index
        largest = index
        # if the value at left or right is larget than the current index reassign largest
        if self.storage[largest] < self.storage[left]:
            largest = left
        if self.storage[largest] < self.storage[right]:
            largest = right
        # if the largest is now not the original index, swap and recursively call sift down
        # until the largest is at the index
        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)

# insert adds the input value into the heap, method should ensure that inserted value
# is in the correct spot in the heap
#
# delete removes and returns the 'topmost' value from the heap; this method needs to
# ensure that the heap property is maintained after the topmost element is removed
#
# get_max returns the max value in the heap in constant time
#
# _bubble_up moves the element at the specified index "up" the heap by swapping
# it with its parent if the parent's value is less than the value at the specified index
#
# _sift_down grabs the indicies of this element's children and determines which child has a larger value.
# if the larger child's value is larger than the paren'ts value, the child element is swapped with the parent.
# sometimes refered to as max heapify
#
# easiest way to insert is to add to end of array and bubble up to its proper position
#
# to get_max, O(n), return heap at value 1
#
# easiest way to delete is to swap the max value or index 1 with last index, delete
# but also save a max value, sift_down the 1st index which was originally in last index
# to sift, compare child indexes and whatever is the largest swap, and repeat until
# it is in the right position
