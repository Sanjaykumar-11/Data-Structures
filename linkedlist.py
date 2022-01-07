class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def insert_last(self, data):
        if not self.isEmpty():
            new_node = Node(data)
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref =new_node


    def insert_middle(self, data, element):
        n = self.head
        while n is not None:
            if element==n.data:
                break
            else:
                n = n.ref
        if n is not None:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        else:
            print("Element is not Found")

    def delete_begining(self):
        if not self.isEmpty():
            self.head = self.head.ref
        else:
            print("LinkedList is Empty")
    
    def delete_middle(self, element):
        if self.head.ref == None:
            self.head.data = None
            
        elif not self.isEmpty():
            n = self.head
            while n is not None:
                if n.ref.data == element:
                    break
                else:
                    n = n.ref
            n.ref = n.ref.ref
    

        else:
            print("There is no elements in the linked list")



    def delete_last(self):
        if not self.isEmpty():
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

        elif self.head.ref==None:
            self.head.data = None
            
        else:
            print("Nothing to delete")

    def display(self):
        if not self.isEmpty():
            n = self.head
            while n is not None:
                print(n.data, end=" --> ")
                n = n.ref
            print()
        else:
            print("LinkedList is Empty")

LL = LinkedList()
LL.insert_begin(10)
LL.insert_begin(11)
LL.insert_last(999)
LL.insert_last(125)
LL.insert_middle(881, 10)
LL.display()
# LL.delete_begining()
# LL.delete_last()
LL.delete_middle(881)
LL.display()

