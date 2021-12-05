from .node import Node

class UnorderList:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while not (current is None):
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found


    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


    def append(self, item):
        current = self.head
        node = Node(item)

        while current:
            previous = current
            current = current.get_next()

        previous.set_next(node)

    def index(self, item):
        index = 0

        current = self.head
        found = False

        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                index = index + 1

        if current is None:
            index = None

        return index

    def insert(self, pos, item):
        index = 0
        current = self.head
        previous = None
        found = False
        node = Node(item)

        while current != None and not found:
            if index == pos:
                found = True
            else:
                previous = current
                current = current.get_next()
                index = index + 1

        if previous is None:
            node.set_next(current)
            self.head = node
        else:
            node.set_next(current)
            previous.set_next(node)

        return None if not found else node


    def pop(self, del_index=None):
        index = 0
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if index == del_index or current.get_next() == del_index:
                # del current
                found = True
            else:
                previous = current
                current = current.get_next()
                index = index + 1

        if current is None:
            raise 'IndexOut'

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current


    def __str__(self):
        if self.head:
            return str(self.head.get_data())
        return ''

    def __iter__(self):
        current = self.head
        while current:
            yield current.get_data()
            current = current.get_next()
