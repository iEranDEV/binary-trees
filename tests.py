import balance
import utils
import timeit
import sys

sys.setrecursionlimit(10**9)

sizes = [25, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]

arrays = {}
trees = {
    "avl": {},
    "bst": {}
}
ile_ciagow = 1

# Generowanie ciągów
for size in sizes:
    arrays[size] = []
    for i in range(ile_ciagow):
        arrays[size].append(utils.generate_decreasing_sequence(size, 150000))

# Generowanie drzew
print("GENEROWANIE DRZEW")
for size in sizes:
    tempArrayAVL = []
    tempArrayBST = []
    print(f'  n = {size}')
    avl_avg = 0
    bst_avg = 0
    for array in arrays[size]:
        array.sort()
        t0_AVL = timeit.default_timer()
        treeAVL = utils.createAVL(array)
        t1_AVL = timeit.default_timer()
        avl_avg += (t1_AVL - t0_AVL)

        t0_BST = timeit.default_timer()
        treeBST = utils.createRandomBST(array)
        t1_BST = timeit.default_timer()
        bst_avg += (t1_BST - t0_BST)

        tempArrayAVL.append(treeAVL)
        tempArrayBST.append(treeBST)
    if bst_avg != 0:
        print('    bst = {:.6f}s'.format(bst_avg / ile_ciagow))
    if avl_avg != 0:
        print('    avl = {:.6f}s'.format(avl_avg / ile_ciagow))
    trees["avl"][size] = tempArrayAVL
    trees["bst"][size] = tempArrayBST

print("SZUKANIE MINIMUM")
for size in sizes:
    print(f'  n = {size}')
    avl_avg = 0
    bst_avg = 0
    for tree in trees["avl"][size]:
        t0_AVL = timeit.default_timer()
        tree.findMin(False)
        t1_AVL = timeit.default_timer()
        avl_avg += (t1_AVL - t0_AVL)
    for tree in trees["bst"][size]:
        t0_BST = timeit.default_timer()
        tree.findMin(False)
        t1_BST = timeit.default_timer()
        bst_avg += (t1_BST - t0_BST)
    if bst_avg != 0:
        print('    bst = {:.10f}s'.format(bst_avg / ile_ciagow))
    if avl_avg != 0:
        print('    avl = {:.10f}s'.format(avl_avg / ile_ciagow))

print("RÓWNOWAŻENIE DRZEWA")
for size in sizes:
    print(f'  n = {size}')
    bst_avg = 0
    for tree in trees["bst"][size]:
        t0_BST = timeit.default_timer()
        balance.balanceBST(tree)
        t1_BST = timeit.default_timer()
        bst_avg += (t1_BST - t0_BST)
    if bst_avg != 0:
        print('    bst = {:.6f}s'.format(bst_avg / ile_ciagow))
