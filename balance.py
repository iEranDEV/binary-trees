import math
from node import Node


def bstToVine(grand):
    count = 0
    tmp = grand.right
    while tmp:
        if tmp.left:
            oldTmp = tmp
            tmp = tmp.left
            oldTmp.left = tmp.right
            tmp.right = oldTmp
            grand.right = tmp
        else:
            count += 1
            grand = tmp
            tmp = tmp.right
    return count


def compress(grand, m):
    tmp = grand.right
    for i in range(m):
        oldTmp = tmp
        tmp = tmp.right
        grand.right = tmp
        oldTmp.right = tmp.left
        tmp.left = oldTmp
        grand = tmp
        tmp = tmp.right


def balanceBST(root):
    grand = Node(0)
    grand.right = root
    count = bstToVine(grand)
    h = int(math.log2(count + 1))
    m = pow(2, h) - 1
    compress(grand, count - m)
    for m in [m // 2 ** i for i in range(1, h + 1)]:
        compress(grand, m)
    return grand.right
