from node import node

class LinkedList:
	def __init__(self):
		#should accept lists and tuples
		self.front=self.end=None
		self.size=0

        def append(x):
                new_node=Node(x,None)
                if self.front is None:
                        self.front = self.end = new_node
                else:
                        self.end.next=new_node
                        self.end=new_node
                self.size+=1
        
        def extend(L):
                pass

        def insert(i,x):
                if i>self.size or i<0:
                        raise IndexError("{} index out of range".format(self.__name__))
                prv=None
                ptr=self.front
                while i is not 0:
                        prv=ptr
                        ptr=ptr.next
                new_node = Node(x,ptr)
                if i is 0:
                        self.front = new_node
                if i is self.size:
                        self.end = new_node
                if prv is not None:
                        prv.next=new_node
                self.size+=1
                        
        def remove(x):
                ptr=self.front
                

        def pop(i=None):
                pass

        def index(x):
                pass

        def count(x):
                pass

        def sort(cmp=None,key=None,reverse=False):
                pass

        def reverse():
                pass
                
class DoublyLL:
        def __init__(self):
                pass

class CircularLL:
        def __init__(self):
                pass
