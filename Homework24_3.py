class Stack:
    def __init__(self):
        self.__items = []

    def push(self, new_item):
        self.__items.append(new_item)

    def pop(self):
        return self.__items.pop()

    def get(self):
        return self.__items[-1]

    def __str__(self):
        return str(self.__items)

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)

    def get_from_stack(self, e):
        temp_stack = []
        found = False

        while self.__items:
            top_item = self.pop()
            if top_item == e:
                found = True
                break
            temp_stack.append(top_item)

        if not found:
            while temp_stack:
                self.push(temp_stack.pop())
            raise ValueError(f"Element {e} not found in {self.__class__.__name__}")

        while temp_stack:
            self.push(temp_stack.pop())

        return e


class Queue:
    def __init__(self):
        self.__items = []

    def push(self, new_item):
        self.__items.append(new_item)

    def pop(self):
        return self.__items.pop(0)

    def get(self):
        return self.__items[0]

    def __str__(self):
        return str(self.__items)

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)

    def get_from_queue(self, e):
        temp_queue = []
        found = False

        while self.__items:
            front_item = self.pop()
            if front_item == e:
                found = True
                break
            temp_queue.append(front_item)

        if not found:
            while temp_queue:
                self.push(temp_queue.pop(0))
            raise ValueError(f"Element {e} not found in {self.__class__.__name__}")

        while temp_queue:
            self.push(temp_queue.pop(0))

        return e
