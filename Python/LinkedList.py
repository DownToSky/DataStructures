from Node import Node

class LinkedList:
    def __init__(self,l=None):
        self.front=self.end=None
        self.size=0
        if isinstance(l,list) or isinstance(l,tuple):
            for e in l:
                self.append(e)

    def append(self,x):
        """
        Appends x at the end of the linked list
        """
        new_node=Node(x,None)
        if self.front is None:
                self.front = self.end = new_node
        else:
                self.end.next=new_node
                self.end=new_node
        self.size+=1
    
    def extend(self,L):
        """
        Appends L to the end of the linked list
        """
        #to do: why doesn't __name__ not work
        if not isinstance(L,LinkedList):
            raise ValueError("L is a class type'{}'".format("LinkedList"))
        #to do: explain that it alls the other list and does not make a new list (maybe change that behaviour)        
        if L.front is None: #L has no nodes
            return
        if self.front is None: #This class instance has no nodes
            self.front= L.front
            self.end=L.end
            self.size=L.size
        else:
            self.end.next=L.front
            self.end=L.end
            self.size+=L.size

    def insert(self,i,x):
        """
        Inserts x in the i-th position.
        """
        #to do: why doesn't self.__name__ not work
        if i>self.size or i<0:
                raise IndexError("{} index out of range".format("LinkedList"))
        prv=None
        ptr=self.front
        ctr=0
        while ctr is not i:
                prv=ptr
                ptr=ptr.next
                ctr+=1
        new_node = Node(x,ptr)
        if ctr is 0:
                self.front = new_node
        elif ctr is self.size:
                prv.next=new_node
                self.end = new_node
        else:
                prv.next=new_node
        self.size+=1
                    
    def remove(self,x):
        """
        Removes the first occurence of x in the linked list
        """
        prv=None
        ptr=self.front
        while ptr!=None:
            if ptr.data == x:
                if prv != None:
                    prv.next=ptr.next
            if ptr==self.end:
                self.end=prv
            if ptr==self.front:
                self.front=ptr.next
            self.size-=1
            return
        raise ValueError("{} not found".format(x))

    def pop(self,i=None):
        """
        Removes the i-th element from the linked list. If 
        i was not specified, it will remove the last
        """
        if i is None:
            i=self.size-1
        if i>=self.size or i<0:
            raise IndexError("{} index out of range".format("LinkedList"))
        prv=None
        ptr=self.front
        ctr=0
        while ctr!=i:
            prv=ptr
            ptr=ptr.next
            ctr+=1
        val=ptr.data
        if prv != None:
            prv.next=ptr.next
        if ptr is self.end:
            self.end=prv
        if ptr is self.front:
            self.front=ptr.next
        self.size-=1
        return val

    def clear(self):
        """ Clears the linked list """
        self.head=self.end=None
        self.size=0

    def index(self,x):
        """ Finds the index of first occurence of x in linked list """
        prv=None
        ptr=self.front
        i=0
        while ptr!=None:
            if ptr.data == x:
                return i
            prv=ptr
            ptr=ptr.next
            i+=1
        raise ValueError("{} not found".format(x))

    def count(self,x):
        """ Counts the number of occurences of x in linked list """
        prv=None
        ptr=self.front
        i=0
        while ptr!=None:
            if ptr.data == x:
                i+=1
            prv=ptr
            ptr=ptr.next
        return i

    def sort(self,cmp=None,key=None,reverse=False):
        pass

    def reverse(self):
        """ Reverses the linked list in place """
        newList=LinkedList()
        ptr=self.front
        while ptr!=None:
            newList.append(ptr.data)
            ptr=ptr.next
        self.front=newList.front
        self.end=newList.end
        self.size=newList.size

    def copy(self):
    """ Returns a shallow copy of hte list """
    newList=LinkedList()
    ptr=self.front
    while ptr!=None:
        newList.insert(0,ptr.data)
        ptr=ptr.next
    return newList
            
class DoublyLL:
    def __init__(self):
        pass

class CircularLL:
    def __init__(self):
        pass
