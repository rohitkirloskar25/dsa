class LinkedList:
    def __init__(self, value):
        # initialize the linked list
        # and create a new node
        new_node = Node(value)
        # assign pointers
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        # create a node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def pop(self):
        # edge case 1
        if self.head is None:
            return None
        
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head == None
            self.tail == None
        return temp
        
    def prepend(self, value):
        # create a node
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length-1:
            self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value} -> ", end="")
            temp = temp.next
        print("None\n")

class Node:
    def __init__(self, value):
        # create a node
        self.value = value
        self.next = None
        

my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)

print(f"Length after creating LL: {my_ll.length}")
my_ll.display()
my_ll.prepend(-1)

print(f"Length after prepending: {my_ll.length}")
my_ll.display()
my_ll.pop()

print(f"Length after popping: {my_ll.length}")
my_ll.display()
my_ll.pop_first()

print(f"Length after popping first: {my_ll.length}")
my_ll.display()

print(f"Node at index 4 is : {my_ll.get(4).value}\n")

print(f"After modify index 3 with value two: ")
my_ll.set_value(3, 2)
my_ll.display()

print(f"After inserting at index 4 with value nine: ")
my_ll.insert(4, 9)
print(f"Length after inserting: {my_ll.length}")
my_ll.display()

print(f"After removing at index 2: ")
my_ll.remove(2)
print(f"Length after inserting: {my_ll.length}")
my_ll.display()

print("After reversing the list:")
my_ll.reverse()
my_ll.display()

    