class Node:
    def __init__(self, n):
        self.data = n
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self, node):
        while node:
            print(node.data, end=" ")
            node = node.next

def remove_duplicate_from_sorted_linked_list(head):
    new_head = None
    tail = None
    s = set()
    temp = head
    while temp:
        new_node = temp
        # print(new_node.data)
        if new_node.data not in s:
            # print("initializing new head", new_node.data)
            if new_head is None:
                new_head = temp
                tail = new_head
                s.add(new_head.data)
            else:
                tail.next = new_node
                tail = new_node
                s.add(tail.data)
        temp = temp.next
    # print("set elements")
    # for i in s:
    #     print(i, end=" ")
    # print("\n")
    # print("new_node",new_head.data)
    # print("new_node",new_head.next.data)
    return new_head

def print_unique_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next


a = LinkedList()
for i in [12,11,12,21,5]:
    a.append(i)

# print(a.head.data)
# print(a.head.next.data)
# print(a.head.next.next.data)
a.print_list(a.head)

print("\n")
print("calling method to remove duplicate nodes")
print_unique_list(remove_duplicate_from_sorted_linked_list(a.head))
