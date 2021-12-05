from .node import Node

class OrderList:
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        node = Node(item)
        if previous is None:
            node.set_next(self.head)
            self.head = node
        else:
            node.set_next(current)
            previous.set_next(node)


    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if not found:
            return None

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current


    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found


    def empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head

        while current != None:
            current = current.get_next()
            count = count + 1

        return count

    def index(self, item):
        index = 0
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() > item:
                stop = True
            else:
                if current.get_data() == item:
                    found = True
                else:
                    current = current.get_next()
                    index = index + 1

        return None if current is None else index

    def pop(self, pos=None):
        index = 0
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if index == pos:
                found = True
            else:
                previous = current
                current = current.get_next()
                index = index + 1

        if current is None:
            return None

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.get_next()

