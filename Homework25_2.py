class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_node = self.top
        self.top = self.top.next_node
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size

    def __str__(self):
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next_node
        return "[" + ", ".join(map(str, result)) + "]"


stack = Stack()
print(stack)

stack.push(10)
stack.push(20)
stack.push(30)
print(stack)

print(stack.pop())
print(stack)

print(stack.peek())
print(len(stack))

stack.pop()
stack.pop()
print(stack.is_empty())
