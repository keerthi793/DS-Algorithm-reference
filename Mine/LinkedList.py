'''
Node:
Create a new node for list whenever invoked.
'''
class Node:
    def __init__(self,  ):
        self.data = data # element in the node
        self.next = None # Pointer to the next node
		

'''
Linked list
Methods:Insert, InsertEnd, printList, delete
'''
class LinkedList:
    def __init__(self):
        self.head = None # To track the first element of the list
        self.tail = None # To track the last element of the list
        self.size = 0 # To track the size of the list
		
    '''
    Inserts the element at the begining of the list
    * Create new node for the new element
    * Store the head pointer to a temporary variable
    * Make the new node points to the header and change the new node as head
    '''
    def insert(self, element):
        new = Node(element)
        temp = self.head
        self.head = new
        new.next = temp
        self.size += 1
        if self.size == 1:
            self.tail = self.head
			
    '''
    Inserts the element at the end of the list
    * Create new node for the new element
    * Store the tail pointer to a temporary variable
    * Make the new node points to null and change the new node as tail
    '''
    def insertEnd(self, element):
       new = Node(element)
       temp = self.tail
       self.tail.next = new
       self.tail = new
       self.size += 1 
	          
	''' 
	Delete a node:
	* Find the element
	* Make the previous node of delete element points to the next node of the delete element.
	'''   
	def delete(self, element):
		temp = self.head        
		prev = None        
		while temp != None:            
		if temp.data == element:                
			if prev == None: # case 1: if element at the start                    
				self.head = temp.next                
			elif temp.next == None: # case 2: if element at the end                    
				prev.next = None                
			else: # case 3: if element is present inbetween                    
				prev.next = temp.next                
			self.size -= 1            
		prev = temp            
		temp = temp.next
		        
	'''
	Print list:    
	* Loop and print the elements of the list    
	'''    
	def printList(self):        
		temp = self.head        
		while temp != None:            
			print(temp.data)            
			temp = temp.next
			
    ''' 
	Print size:    
	* Print the size of the list with the help of size tracker    
	'''    
	def getSize(self):        
	return self.size    # Main function to check the linked list
	
if __name__ == "__main__":    
	a = LinkedList()    
	a.insert(3)    
	a.insert(4)    
	a.insert(6)    
	a.insert(9)    
	a.insert(10)    
	a.insertEnd(5)    
	a.delete(4)    
	a.printList()   
	print("Size of the list:",a.getSize())

			
			