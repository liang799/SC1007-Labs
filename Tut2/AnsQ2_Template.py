class ListNode:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
 
    def print_list(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return 0
        prev_node = self.find_node(index - 1)
        if prev_node is None:
            return -1
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return 0

    def remove_node(self, index):
        if self.head is None:
            return -1
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return 0
        prev_node = self.find_node(index - 1)
        if prev_node is None or prev_node.next is None:
            return -1
        prev_node.next = prev_node.next.next
        self.size -= 1
        return 0

    def remove_all_items(self):
        self.head = None
        self.size = 0

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.insert_node(0, item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.item

    def is_empty(self):
        return self.ll.size == 0

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        self.ll.insert_node(self.ll.size, item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def is_empty(self):
        return self.ll.size == 0

def reverse_first_k_items(queue, k):
    s = Stack()
    for i in range(k):
        s.push(queue.dequeue())

    tmp = Queue()
    while not queue.is_empty():
        item = queue.dequeue()
        tmp.enqueue(item)

    while not s.is_empty():
        queue.enqueue(s.pop())

    current = queue.ll.head
    while current.next is not None:
        current = current.next

    tail = current

    tail.next = tmp.ll.head

def main():
    q = Queue()
    for i in range(1,6):
        q.enqueue(i)

    print("initial: ")
    q.ll.print_list()

    print("\nfinal: ")
    reverse_first_k_items(q, 3)
    q.ll.print_list()

if __name__ == "__main__":
    main()