
# python3 Program to print zigzag traversal of binary tree
import collections
# Binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# function to print vertical order traversal of binary tree
def verticalTraverse(root):

    # Base case
    if root is None:
        return

    # Create empty queue for level order traversal
    queue = []

    # create a map to store nodes at a particular
    # horizontal distance
    m = {}

    # map to store horizontal distance of nodes
    hd_node = {}

    # enqueue root
    queue.append(root)
    # store the horizontal distance of root as 0
    hd_node[root] = 0

    m[0] = [root.data]

    # loop will run while queue is not empty
    while len(queue) > 0:

        # dequeue node from queue
        temp = queue.pop(0)

        if temp.left:
            # Enqueue left child
            queue.append(temp.left)

            # Store the horizontal distance of left node
            # hd(left child) = hd(parent) -1
            hd_node[temp.left] = hd_node[temp] - 1
            hd = hd_node[temp.left]

            if m.get(hd) is None:
                m[hd] = []

            m[hd].append(temp.left.data)

        if temp.right:
            # Enqueue right child
            queue.append(temp.right)

            # store the horizontal distance of right child
            # hd(right child) = hd(parent) + 1
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right]

            if m.get(hd) is None:
                m[hd] = []

            m[hd].append(temp.right.data)

    # Sort the map according to horizontal distance
    sorted_m = collections.OrderedDict(sorted(m.items()))

    # Traverse the sorted map and print nodes at each horizontal distance
    for i in sorted_m.values():
        for j in i:
            print(j, " ", end ="")
        print()

# Driver program to check above function
"""
Constructed binary tree is 
            1
        / \
        2     3
    / \ / \
    4     5 6     7
            \ / \
            8 10 9
                \
                11
                    \ 
                    12
                
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)
print("Vertical order traversal is ")
verticalTraverse(root)

# This code is contributed by Shweta Singh

