# python3

import sys
import threading
import os
import numpy

def compute_height(n, parents):
    nodes = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    max_height = 0
    def depth(node):
        if not nodes[node]:
            return 1
        else:
            height = [depth(child) for child in nodes[node]]
            return 1 + max(height)

    max_height = depth(root)
    return max_height


def main():
    u_input = input().strip()
    if os.path.isfile(u_input):
        input_file = open(u_input, 'r')
        n = int(input_file.readline().strip())
        parents = list(map(int, input_file.readline().strip().split()))
    else:
        n = int(u_input)
        parents = list(map(int, input().split()))
    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
