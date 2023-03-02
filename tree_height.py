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
    method = input().strip()
    if method == "I":
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
    elif method == "F":
        file_name = input().strip()
        if os.path.isfile(file_name):
            in_file = open("./test/" + file_name, 'r')
            n = int(in_file.readline().strip())
            parents = list(map(int, in_file.readline().strip().split()))
    
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
