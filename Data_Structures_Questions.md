Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(1)

2. What is the runtime complexity of `dequeue`?
   O(1)

3. What is the runtime complexity of `len`?
   O(1)

## Binary Search Tree

essentially it would become a single-linked list for worst case

1. What is the runtime complexity of `insert`?
   average: O(log n), worst case: O(n)

2. What is the runtime complexity of `contains`?
   average: O(log n), worst case: O(n)

3. What is the runtime complexity of `get_max`?
   average: O(log n), worst case: O(n)

## Heap

1. What is the runtime complexity of `_bubble_up`?
   O(log n)
2. What is the runtime complexity of `_sift_down`?
   O(log n)
3. What is the runtime complexity of `insert`?
   O(log n)
4. What is the runtime complexity of `delete`?
   O(log n)
5. What is the runtime complexity of `get_max`?
   O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
   O(1)
3. What is the runtime complexity of `ListNode.delete`?
   O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

doubly linked list is O(1) because regardless of the input n, it just deletes the requested
node, it may then change the pointers, but that is still going to be constant
The Array.splice can be O(n) due to changing the index aftext splicing, it has to move
all of the elements in the array by shifting them over after the splice
