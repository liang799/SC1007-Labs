class BTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class StackNode:
    def __init__(self, btnode):
        self.btnode = btnode
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

def createBTNode(item):
    return BTNode(item)

def push(stk, node):
    temp = StackNode(node)
    if stk.top is None:
        stk.top = temp
        temp.next = None
    else:
        temp.next = stk.top
        stk.top = temp

def pop(stk):
    if stk.top is None:
        return None
    
    temp = stk.top.next
    ptr = stk.top.btnode
    stk.top = temp
    return ptr

def printTree(node):
    if node is None:
        return
    printTree(node.left)
    print(node.item, end=" ")
    printTree(node.right)

def createTree():
    stk = Stack()
    root = None

    print("Input an integer that you want to add to the binary tree. Any Alpha value will be treated as NULL.")
    try:
        item = input("Enter an integer value for the root: ")
        root = createBTNode(int(item))
        push(stk, root)
    except ValueError:
        return None

    while True:
        temp = pop(stk)
        if temp is None:
            break

        try:
            item = input(f"Enter an integer value for the Left child of {temp.item}: ")
            temp.left = createBTNode(int(item))
        except ValueError:
            temp.left = None

        try:
            item = input(f"Enter an integer value for the Right child of {temp.item}: ")
            temp.right = createBTNode(int(item))
        except ValueError:
            temp.right = None

        if temp.right is not None:
            push(stk, temp.right)
        if temp.left is not None:
            push(stk, temp.left)

    return root

def removeAll(node):
    if node is not None:
        removeAll(node.left)
        removeAll(node.right)
        node.left = None
        node.right = None


class BTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


# ... (Stack and StackNode classes remain the same) ...

def maxDepth(node):
    if node is None:
        return -1
    l = 1 + maxDepth(node.left)
    r = 1 + maxDepth(node.right)
    return max(r, l)


def printTree(node):
    """Helper to visualize the tree (In-order traversal)"""
    if node is None:
        return
    printTree(node.left)
    print(node.item, end=" ")
    printTree(node.right)


def build_tree_from_list(elements):
    """
    Automates tree creation from a list.
    Example: [1, 2, 3, None, 4]
    """
    if not elements or elements[0] is None:
        return None

    root = BTNode(elements[0])
    queue = [root]
    i = 1
    while i < len(elements):
        current = queue.pop(0)

        # Left Child
        if i < len(elements) and elements[i] is not None:
            current.left = BTNode(elements[i])
            queue.append(current.left)
        i += 1

        # Right Child
        if i < len(elements) and elements[i] is not None:
            current.right = BTNode(elements[i])
            queue.append(current.right)
        i += 1
    return root


def run_tests():
    # Format: (List Representation, Expected Depth, Test Name)
    test_cases = [
        ([1, 2, 3, 4, 5], 2, "Balanced Tree"),
        ([1, 2, None, 3, None, 4], 3, "Left-Skewed Tree"),
        ([1], 0, "Single Node"),
        ([], -1, "Empty Tree"),
        ([1, 2, 3, None, None, None, 4], 2, "Asymmetric Tree")
    ]

    print(f"{'Test Name':<20} | {'Expected':<10} | {'Actual':<10} | {'Result'}")
    print("-" * 60)

    for data, expected, name in test_cases:
        root = build_tree_from_list(data)
        actual = maxDepth(root)
        status = "PASS" if actual == expected else "FAIL"
        print(f"{name:<20} | {expected:<10} | {actual:<10} | {status}")


if __name__ == "__main__":
    run_tests()
