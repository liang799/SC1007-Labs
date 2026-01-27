class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    The head reference is essential
    to locate the first node in the list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  
        
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
            
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return True
        
        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            if index == self.size: self.tail = new_node
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            return False
            
        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

def moveOdditemstoback(head):
    odd_list = LinkedList()
    even_list = LinkedList()
    current = head

    even_head = None
    odd_head = None

    while current is not None:
        if current.data % 2 == 0:
            if even_head is None:
                even_head = current
                even_list.insertNode(current.data, 0)
            else:
                size = even_list.size
                even_list.insertNode(current.data, size)
        else:
            if odd_head is None:
                odd_head = current
                odd_list.insertNode(current.data, 0)
            else:
                size = odd_list.size
                odd_list.insertNode(current.data, size)

        current = current.next

    even_list.tail.next = odd_list.head

    return even_list.head

def moveOdditemstoback_v1(head):
    odd_even_separation = LinkedList()
    if head is None:
        return odd_even_separation

    print(head.data)

    odd_even_separation.insertNode(head.data, 0)
    current = head

    while current.next != None:
        current = current.next

        print(current.data)

        if current.data % 2 != 0:
            current_size = odd_even_separation.size
            odd_even_separation.insertNode(current.data, current_size)
        else:
            odd_even_separation.insertNode(current.data, 0)

    return odd_even_separation.head

if __name__ == "__main__":
    linked_list = LinkedList()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break

    print("\nBefore:", end=" ")
    linked_list.printList()
    linked_list.head = moveOdditemstoback(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()