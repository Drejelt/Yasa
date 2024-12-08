class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if not self.front:
            raise IndexError("Dequeue from empty queue")
        dequeued_data = self.front.data
        self.front = self.front.next_node
        if not self.front:
            self.rear = None
        self.size -= 1
        return dequeued_data

    def peek(self):
        if not self.front:
            raise IndexError("Peek from empty queue")
        return self.front.data

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __str__(self):
        current = self.front
        s = "["
        while current:
            s += str(current.data) + (", " if current.next_node else "")
            current = current.next_node
        s += "]"
        return s



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)

print(queue.dequeue())
print(queue)

queue.enqueue(4)
print(queue)

print(queue.peek())

print(queue.is_empty())

print(len(queue))
