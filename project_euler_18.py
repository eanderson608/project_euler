# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is,  3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                75
#               95 64
#              17 47 82
#             18 35 87 10
#            20 04 82 47 65
#           19 01 23 75 03 34
#          88 02 77 73 07 63 67
#         99 65 04 28 06 16 70 92
#        41 41 26 56 83 40 80 70 33
#       41 48 72 33 47 32 37 16 94 29
#      53 71 44 65 25 43 91 52 97 51 14
#     70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
#  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# a node object that has a value and two children
class BinaryNode:

    left_child = None
    right_child = None
    coords = None

    def __init__(self, value):
        self.value = value


from collections import deque

tree = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 04, 82, 47, 65],
    [19, 01, 23, 75, 03, 34],
    [88, 02, 77, 73, 07, 63, 67],
    [99, 65, 04, 28, 06, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
    ]

root = BinaryNode(tree[0][0]) # define root node
root.coords = (0, 0) # set corrdinates in tree
queue = deque([root]) # initialize the queue

max_path = 0 # variable to hold maximum path total found so far

# bfs mapping of tree while simultaneously computing path size
while len(queue) > 0:

    # pop next item from queue
    curr = queue.popleft()

    if curr.coords[0] < 14:
        i, j = curr.coords

        # store the value of child plus value of parent.  then leaf nodes will contain total value of path
        curr.left_child = BinaryNode(tree[i + 1][j] + curr.value)
        if curr.left_child.value > max_path:
            max_path = curr.left_child.value
        curr.right_child = BinaryNode(tree[i + 1][j + 1] + curr.value)
        if curr.right_child.value > max_path:
            max_path = curr.right_child.value
        curr.left_child.coords = (i + 1, j)
        curr.right_child.coords = (i + 1, j + 1)
        queue.append(curr.left_child)
        queue.append(curr.right_child)

print total
