class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class UnsortedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        self.size += 1

    def index(self, data):
        current = self.root
        current_index = 0

        while current:
            if current.data == data:
                return current_index
            current = current.next_node
            current_index += 1

        raise ValueError(f"{data} is not in the list")

    def pop(self, index=None):
        if self.root is None:
            raise IndexError("pop from empty list")

        if index is None:
            index = self.size - 1

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            popped_node = self.root
            self.root = self.root.next_node
            self.size -= 1
            return popped_node.data

        current = self.root
        current_index = 0
        while current and current_index < index - 1:
            current = current.next_node
            current_index += 1

        popped_node = current.next_node
        current.next_node = popped_node.next_node
        self.size -= 1
        return popped_node.data

    def insert(self, data, index):
        new_node = Node(data)

        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            new_node.next_node = self.root
            self.root = new_node
        else:
            current = self.root
            current_index = 0

            while current and current_index < index - 1:
                current = current.next_node
                current_index += 1

            new_node.next_node = current.next_node
            current.next_node = new_node

        self.size += 1

    def slice(self, start, stop):
        if start < 0 or stop > self.size or start > stop:
            raise IndexError("Invalid slice range")

        sliced_list = UnsortedList()
        current = self.root
        current_index = 0

        while current and current_index < stop:
            if current_index >= start:
                sliced_list.append(current.data)
            current = current.next_node
            current_index += 1

        return sliced_list

    def __str__(self):
        elements = []
        current = self.root
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return "[" + ", ".join(elements) + "]"

x = UnsortedList()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
x.append(6)
x.append(7)
print(x)
print(x.index(2))
print('-----')
print(x.pop(2))
print(x)
print(x.slice(0, 5))