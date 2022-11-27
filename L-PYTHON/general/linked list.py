# Creating Linked list
class Node:
    def __init__(self, data=None):
        self.data = data        # initializing data
        self.next = None        # initializing next

class LinkedList:
    def __init__(self):
        self.head = None        # head node is initially none

    # To display the elements of Linked List
    def display(self):
        p = self.head
        A = []
        while p != None:
            A.append(p.data)
            p = p.next
        print(A)

    def search(self, val):
        p = self.head
        while p != None:
            if val == p.data:
                print(p.data, " is in the linked list")
                break
            p = p.next
        if p == None:
                print(val, "is not in the linked list")

    def InsertBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

    def InsertEnd(self, newdata):
        NewNode = Node(newdata)
        p = self.head
        if p is None:
            p = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = NewNode

    # Function to add node after a element
    def Inbetween(self, mid, newdata):
        if mid is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.next = mid.next
        mid.next = NewNode

    # Function to remove node
    def RemoveNode(self, val):
        p = self.head
        if (p is not None):
            if (p.data == val):
                self.head = p.next
                Head = None
                return
        while (p is not None):
            if p.data == val:
                break
            prev = p
            p = p.next
        if (p == None):
            return
        prev.next = p.next
        p = None

    def sum(self):
        p = self.head
        a = 0
        while p != None:
            a = a+p.data
            p = p.next
        print("Sum is : " ,a)

    def CheckDelete(self, val):
        p = self.head
        while p != None:
            if val == p.data:
                if (p is not None):
                    if (p.data == val):
                        self.head = p.next
                        Head = None
                        return
                while (p is not None):
                    if p.data == val:
                        break
                    prev = p
                    p = p.next
                if (p == None):
                    return
                prev.next = p.next
                p = None
                break
            p = p.next
        if p == None:
            print(val, " is not in the linked list so can't delete it")


    def AddingLinked(self, list):
        p = self.head
        val = list.head
        A = []
        while p != None:
            A.append(val.data)
            p = p.next
        print(A)










list = LinkedList()
list.head = Node(10)
e2 = Node(20)
list.head.next = e2

list.InsertEnd(200)
list.InsertBegining(100)
list.Inbetween(list.head,5)
list.RemoveNode(5)
list.display()
list.search(2000)
list.sum()
#list.CheckDelete(1000)


# driver function to add linked list
#list.CheckDelete(100)
list.AddingLinked(list)
list.display()
print("mandik")