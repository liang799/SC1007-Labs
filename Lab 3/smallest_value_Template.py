class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        
def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def smallest_value_original(node):
    if node.left is None and node.right is None:
        return node.item

    if node.left is None:
        return node.item

    smallest = smallest_value_original(node.left)
    if node.item < smallest:
        smallest = node.item

    if node.right is None:
        return smallest
    current = smallest_value_original(node.right)
    if current < smallest:
        smallest = current

    return smallest


def smallest_value(node):
    # Base case: If the node is None, return infinity
    # so it does not interfere with the min() calculation.
    if node is None:
        return float('inf')

    # Recursively find the smallest values in both subtrees
    left_smallest = smallest_value(node.left)
    right_smallest = smallest_value(node.right)

    # Return the minimum among the current node, left subtree, and right subtree
    return min(node.item, left_smallest, right_smallest)

def run_strict_tests(smallest_val_func):
    print("Running strict test cases...\n")

    # Test 1: Standard Tree (Mix of left and right)
    #       4
    #      / \
    #     5   2
    #      \   \
    #       6   1
    t1 = BTNode(4, BTNode(5, None, BTNode(6)), BTNode(2, None, BTNode(1)))
    print(f"Test 1 (Standard): Expected 1, Got {smallest_val_func(t1)}")

    # Test 2: Missing Left Child, Minimum on Right (Your previous flaw)
    #   5
    #    \
    #     2
    #      \
    #       -3
    t2 = BTNode(5, None, BTNode(2, None, BTNode(-3)))
    print(f"Test 2 (Right-Skewed w/ Negatives): Expected -3, Got {smallest_val_func(t2)}")

    # Test 3: Missing Right Child, Minimum on Left
    #       10
    #      /
    #     8
    #    /
    #   4
    t3 = BTNode(10, BTNode(8, BTNode(4)))
    print(f"Test 3 (Left-Skewed): Expected 4, Got {smallest_val_func(t3)}")

    # Test 4: Minimum at the Root
    #       1
    #      / \
    #     9   8
    #    /     \
    #   10      12
    t4 = BTNode(1, BTNode(9, BTNode(10)), BTNode(8, None, BTNode(12)))
    print(f"Test 4 (Root is Min): Expected 1, Got {smallest_val_func(t4)}")

    # Test 5: Single Node Tree
    #   42
    t5 = BTNode(42)
    print(f"Test 5 (Single Node): Expected 42, Got {smallest_val_func(t5)}")

if __name__ == "__main__":
    # Pass your function directly into the test suite
    run_strict_tests(smallest_value)