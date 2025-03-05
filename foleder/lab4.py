class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None  
class SinglyLinkedList:
    def __init__(self):
        self.head = None  

    
    def append_node(self, data):
        new_node = Node(data)  
        
        if self.head is None:
            
            self.head = new_node
        else:
           
            current = self.head
            while current.next:
                current = current.next
           
            current.next = new_node

   
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True  
            current = current.next
        return False 

    
    def display_list(self):
        current = self.head
        if current is None:
            print("The list is empty.")
        else:
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  


if __name__ == "__main__":
   
    linked_list = SinglyLinkedList()
    
    
    linked_list.append_node(10)
    linked_list.append_node(20)
    linked_list.append_node(30)
    
    
    linked_list.display_list() 
    
    
    print(linked_list.search_node(20))  
    print(linked_list.search_node(40))
