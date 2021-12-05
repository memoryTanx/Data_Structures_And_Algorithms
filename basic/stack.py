class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        result = self.items.pop()
        self.items.append(result)
        return result

    def size(self):
        return len(self.items)

    def __next__(self):
        return self.items.pop()

    def __iter__(self):
        while self.size() > 0:
            yield self.items.pop()
