class Node:
    def __init__(self, value):
        # Create a node
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(1)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head

        if index <= (self.length / 2):
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail 
            for _ in range(self.length -1, index, -1):
                temp = temp.prev 
        
        return temp

    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
        
        return True

    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)

            new_node.next = before.next
            new_node.next.prev = new_node

            before.next = new_node
            new_node.prev = before

            self.length += 1

        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.pop_first()

        elif index == self.length:
            return self.pop()

        else:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                before = self.get(index-1)
                temp = self.get(index)
                before.next = temp.next
                temp.next.prev = before
                temp.prev = None
            self.length -= 1

            
        
        return True


        

    def print(self):
        temp = self.head
        while temp is not None:
            print(f" <--> {temp.value}", end='')
            temp = temp.next

        print(f"\nLength: {self.length}")
    

dll = DoublyLinkedList(1)
dll.print()
dll.append(2)
dll.print()
dll.append(3)
dll.print()
dll.append(4)
dll.print()
print("Removing Node: ",dll.pop().value)
dll.print()
print("After prepending")
dll.prepend(0)
dll.print()
print("After popping first")
dll.pop_first()
dll.print()
print("Value at index 0: ",dll.get(0).value)
print("Value at index 2: ",dll.get(2).value)
print("Setting -1 at position 0")
dll.set_value(-1, 0)
dll.print()
print("Inserting 45 at postion 2")
dll.insert(45, 2)
dll.print()
print("Remove value postion 4")
dll.remove(4)
dll.print()