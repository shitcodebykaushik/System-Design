"""Implementation of a singly linked list in Python."""

"""We have two things in the linked list one is The node class which is the container of the data and the othe rthing is the The LinkedList class Which is the manager that connects the nodes"""
"""Each node need to stroe the two things : The data (the value) and the pointer to the next node """

class Node:
    def __init__(self,data):
        self.data = data   # The actual value 
        self.next = None   # Initially,it points to nothing
        
        
        
        """The list itself only need to remember the one things that is  where it start(the head)"""
        
        class LinkedList:
            def __init__(self):
                self.head = None
                
                
            def insert_at_front(self,data):
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
                
        