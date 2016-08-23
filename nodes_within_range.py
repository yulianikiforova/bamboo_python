#Can you augment a BST to return the number
#of elements with node values in a given range?
def nodes_within_range(tree, value1, value2, n):
                if tree != None:
                                if tree.getRootValue() > value1 and tree.getRootValue() < value2:
                                                n += 1
                                if tree.getRootValue() > value1:
                                                n = nodes_within_range(tree.getLeftChild(), value1, value2, n)
                                if tree.getRootValue() < k2:
                                                n = nodes_within_range(tree.getRightChild(), value1, value2, n)
                return n
