# New node class Node:    def __init__(self, data):        self.data = data        self.next = None
# Linked list'''Methods:Insert, InsertEnd, printList'''class LinkedList:    def __init__(self):        self.head = None        self.tail = None        self.size = 0            def insert(self, element):        new = Node(element)        temp = self.head        self.head = new        new.next = temp        self.size += 1        if self.size == 1:            self.tail = self.head        def insertEnd(self, element):        new = Node(element)        temp = self.tail        self.tail.next = new        self.tail = new            def delete(self, element):        temp = self.head        prev = None        while temp != None:            if temp.data == element:                if prev == None:                    self.head = temp.next                elif temp.next == None:                    print(temp)                    prev.next == None                else:                    prev.next = temp.next            prev = temp            temp = temp.next                    def printList(self):        temp = self.head        while temp != None:            print(temp.data)            temp = temp.next            a = LinkedList()a.insert(3)a.insert(4)a.insert(6)a.insert(9)a.insert(10)a.insertEnd(5)a.delete(5)a.printList()
