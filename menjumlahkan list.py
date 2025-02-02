class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while (first is not None or second is not None):
 
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
 
        if carry > 0:
            temp.next = Node(carry)
 
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data),
            temp = temp.next

first = LinkedList()
second = LinkedList()
 
first.push(9)
print ("List pertama =")
first.printList()

second.push(8)
print ("List kedua =")
second.printList()

res = LinkedList()
res.addTwoLists(first.head, second.head)
print ("Hasil penjumlahan Kedua List = ")
res.printList()

