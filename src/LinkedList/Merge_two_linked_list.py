'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):

        a = Node(data)

        if self.head is None:
            self.head = a
            # print(a.data)
            return

        # print("I'm here for your 2nd and afterward node append")
        temp = self.head
        # print('1st time temp out side while loop', temp, temp.data, a.data)
        while temp.next:
            temp = temp.next

        temp.next = a

    def display(self):
        temp = self.head
        # print(temp)
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print(None)


l1 = LinkedList()
l2 = LinkedList()

list1 = []
list2 = []

for i in list1:
    l1.append(i)
l1.display()

for i in list2:
    l2.append(i)
l2.display()
print(type(l2))


def mergeTwoLists(l1, l2):
    if l1.head is None and l2.head is None:
        return l1
    if l1.head is None and l2.head is not None:
        # print("i'm here")
        return l2
    if l1.head is not None and l2.head is None:
        return l1

    l3 = LinkedList()

    temp1 = l1.head
    temp2 = l2.head

    while temp1.next:
        if temp1.data == temp2.data:
            l3.append(temp1.data)
            l3.append(temp2.data)
            print("I'm in 1st branch")
            print(temp1.data)
            print(temp2.data)
        else:
            if temp1.data > temp2.data:
                l3.append(temp2.data)
                l3.append(temp1.data)
                print("I'm in 2nd branch")
                print(temp1.data)
                print(temp2.data)
            elif temp1.data < temp2.data:
                l3.append(temp1.data)
                l3.append(temp2.data)
                print("I'm in 3rd branch")
                print(temp1.data)
                print(temp2.data)
        temp1 = temp1.next
        temp2 = temp2.next

    if temp1.data == temp2.data:
        l3.append(temp1.data)
        l3.append(temp2.data)
    elif temp1.data > temp2.data:
        l3.append(temp2.data)
        l3.append(temp1.data)
    elif temp1.data < temp2.data:
        l3.append(temp1.data)
        l3.append(temp2.data)

    return l3


k = mergeTwoLists(l1, l2)
# print(type(k))
k.display()
