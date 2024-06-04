class Queue:
    def __init__(self, items = None):
        if items is None:
            self.items = []
        elif items:
            self.items = items
        else:
            self.items = []

    @property
    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty:
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty:
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

itmes = [26, 'Salim', 56, "bob"]
queue = Queue(itmes)

queue.enqueue(52)
queue.enqueue("davr")
queue.enqueue(45.3)

print("Queue elementlari:", queue.items)

print("O'chiriladigan element:", queue.dequeue())
print("Element o'chirilgandan keyin:", queue.items)

print("Ishlatiladigan element:", queue.peek())
print("Queue o'lchami:", queue.size())