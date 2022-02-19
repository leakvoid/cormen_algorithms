
# inorder tree walk for binary search trees

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        self.inorder_tree_walk(self.root)
        
    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.left)
            print("parent:", str(x.p), "key:", x.key)
            self.inorder_tree_walk(x.right)

    def tree_search(self, k):
        return self.search(self.root, k)
    
    def search(self, x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def tree_minimum(self):
        return self.minimum(self.root)

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def tree_maximum(self):
        return self.maximum(self.root)

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def tree_successor(self):
        return self.successor(self.root)
        
    def successor(self, x):
        if x.right != None:
            return self.minimum(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y


class Node:
    def __init__(self, parent, left, right, key):
        self.p = parent
        self.left = left
        self.right = right
        self.key = key

    def __str__(self):
        return str(self.key)

root = Node(None, None, None, 6)
bst = BinarySearchTree(root)

ch1_l = Node(root, None, None, 5)
root.left = ch1_l
ch1_r = Node(root, None, None, 7)
root.right = ch1_r

ch2_l = Node(ch1_l, None, None, 2)
ch1_l.left = ch2_l
ch2_r = Node(ch1_l, None, None, 5)
ch1_l.right = ch2_r

ch3_l = Node(ch1_r, None, None, 7)
ch1_r.left = ch3_l
ch3_r = Node(ch1_r, None, None, 8)
ch1_r.right = ch3_r

bst.print_tree()

print("searching for 8")
n = bst.tree_search(8)
if n != None:
    print("node found. parent:", n.p, "key:", n.key)

print("minimum:", bst.tree_minimum())
print("maximum:", bst.tree_maximum())

print("tree successor:", bst.tree_successor())
print("1-d node successor:", bst.successor(ch2_l))
print("3-d node successor:", bst.successor(ch3_r))
