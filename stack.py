class Stack:
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

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty:
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty:
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

items = [25, 26, 86, 37]
stack = Stack(items)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push("ali")
stack.push("bob")
print("Stack: ", stack.items)

stack.pop()
stack.pop()
stack.pop()
print("Pop: ", stack.items)
print("Pop elementi: ", stack.pop())
print("Pop: ", stack.items)

if not stack.is_empty:
    print("Stack elementleri: ",stack.items)
else:
    print("Stack bo'sh!")


print("Ishlatiladigan element:", stack.peek())
print("Stack o'lchami:", stack.size())