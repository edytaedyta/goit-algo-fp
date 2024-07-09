class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def print_list(self):
        values = self.to_list()
        print("->".join(map(str, values)))

def reverse_linked_list(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    # Split the linked list into two halves
    def split(head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    # Merge two sorted linked lists
    def merge(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    left, right = split(head)
    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)
    return merge(left, right)

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# Testing the functions

# Creating a singly linked list
linked_list = SinglyLinkedList()
for value in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
    linked_list.append(value)

print("Original list:")
linked_list.print_list()

# Reversing the singly linked list
linked_list.head = reverse_linked_list(linked_list.head)
print("Reversed list:")
linked_list.print_list()

# Sorting the singly linked list
linked_list.head = merge_sort_linked_list(linked_list.head)
print("Sorted list:")
linked_list.print_list()

# Creating two sorted lists
list1 = SinglyLinkedList()
list2 = SinglyLinkedList()
for value in [1, 3, 5, 7]:
    list1.append(value)
for value in [2, 4, 6, 8]:
    list2.append(value)

print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

# Merging two sorted lists
merged_head = merge_two_sorted_lists(list1.head, list2.head)
merged_list = SinglyLinkedList()
merged_list.head = merged_head
print("Merged list:")
merged_list.print_list()