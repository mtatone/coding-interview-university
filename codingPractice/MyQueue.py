from abc import ABC, abstractmethod


class QueueInterface(ABC):

    @abstractmethod
    def enqueue(self, value):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def peek(self):
        pass


class MyQueue(QueueInterface):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if self.size() > 0:
            return False
        return True

    def peek(self):
        return self.queue[-1]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() < 1:
            return None
        return self.queue.pop(0)

    def print(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


the_queue = MyQueue()
the_queue.enqueue(1)
the_queue.enqueue(21)
the_queue.enqueue(69)
the_queue.print()
print(the_queue.peek())
the_queue.dequeue()
the_queue.print()

