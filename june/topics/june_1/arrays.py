# Python doesn't have a built-in linked list, so we build one
class Node:
    def __init__(self, value):  # each node has a value and a pointer to the next node
        self.value = value  # the data stored in the node
        self.next = None  # pointer to next node


class LinkedList:
    def __init__(self):  # the linked list itself has a pointer to the head node
        self.head = None  # entry point of the list

    def append(
        self, value
    ):  # add a new node with the given value to the end of the list
        new_node = Node(value)  # create a new node with the value
        if not self.head:  # if the list is empty, set the head to the new node
            self.head = new_node  # set head to new node
            return
        # walk to the end
        current = self.head  # start at the head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" → ")
            current = current.next
        print("None")

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


ll = LinkedList()
ll.append(20)
ll.append(30)
ll.prepend(10)  # should give: 10 → 20 → 30 → None
ll.print_list()
ll.delete(20)  # should give: 10 → 30 → None
ll.print_list()
