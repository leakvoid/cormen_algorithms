
class Node:
    def __init__(self, val, parent, left_child, right_sibling):
        self.val = val
        self.parent = parent
        self.left_child = left_child
        self.right_sibling = right_sibling

    def __str__(self):
        return str(self.val)

class UnboundedTree:
    def __init__(self, val):
        node = Node(val, None, None, None)
        self.root = node

    def add_node(self, tree_pos, val):
        i_node = self.root
        for i_pos in range(len(tree_pos)):
            if i_node.left_child != None:
                i_node = i_node.left_child
            for j in range(tree_pos[i_pos]):
                if i_node.right_sibling != None:
                    i_node = i_node.right_sibling

        if tree_pos[-1] == 0:
            new_node = Node(val, i_node, None, None)
            i_node.left_child = new_node
            print("added left:", i_node.val, i_node.parent, i_node.left_child, i_node.right_sibling)
        else:
            new_node = Node(val, i_node.parent, None, None)
            i_node.right_sibling = new_node
            print("added right", i_node.val, i_node.parent, i_node.left_child, i_node.right_sibling)

    def rec_str(self, node):
        if node.parent == None:
            res = "root:"
        else:
            res = "\nparent(" + str(node.parent) + "):"
        delayed_res = ""
        
        i_node = node
        while True:
            res += str(i_node) + ","
            if i_node.left_child != None:
                delayed_res += self.rec_str(i_node.left_child)

            if i_node.right_sibling == None:
                break;
            i_node = i_node.right_sibling

        return res + delayed_res
            
    def __str__(self):
        return self.rec_str(self.root)

u_tree = UnboundedTree(7)
u_tree.add_node([0], 23)
u_tree.add_node([0, 0], 230)
u_tree.add_node([1], 45)
u_tree.add_node([2], 76)
u_tree.add_node([0, 1], 234)
u_tree.add_node([1, 0], 453)
u_tree.add_node([1, 1], 454)
u_tree.add_node([1, 2], 455)
u_tree.add_node([1, 2, 0], 4550)
u_tree.add_node([0, 1, 0], 2340)
u_tree.add_node([1, 2, 0, 0], 45500)
u_tree.add_node([1, 2, 1], 4551)
print(u_tree)
