class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.top is None:
            return None
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        
        return temp

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value, end = ' -> ')
            temp = temp.next
        print()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


my_stack = Stack(4)
my_stack.print_stack()

print("Pushing the value 5")
my_stack.push(5)
my_stack.print_stack()

print("Popping now:")
my_stack.pop()
my_stack.print_stack()

