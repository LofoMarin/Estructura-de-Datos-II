class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# CLASS: BINARY TREE


class BinaryTree:
    def __init__(self, root_data=0):
        self.root = Node(root_data)

    def getLevel(self, root, node, level=1):
        if root == None:
            return 0

        if root == node:
            return level

        downlevel = self.getLevel(root.left, node, level + 1)

        if downlevel != 0:
            return downlevel

        downlevel = self.getLevel(root.right, node, level + 1)

        return downlevel

# TRAVERSALS

    # Method to print inorder traversal
    def inorderTraversal(self, node):
        if node == None:
            return

        self.inorderTraversal(node.left)
        print(node.data, end=' ')
        self.inorderTraversal(node.right)

    # Method to print preorder traversal
    def preorderTraversal(self, node):
        if node == None:
            return

        print(node.data, end=' ')
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)

    # Method to print postorder traversal
    def postorderTraversal(self, node):
        if node == None:
            return

        self.postorderTraversal(node.left)
        self.postorderTraversal(node.right)
        print(node.data, end=' ')

    # Aux. method to print the uncles of a node
    def printUncles(self, root, level, node):
        if root == None:
            return

        if level == 1:
            if (root.left != node and root.right != node):
                print(root.data, end=' ')
        elif level > 1:
            self.printUncles(root.left, level-1, node)
            self.printUncles(root.right, level-1, node)

    # Method to find the uncle of a node
    def findUncles(self, root, node):
        if root == None:
            print('None')
            return

        node_level = self.getLevel(root, node)

        if node_level > 2:
            self.printUncles(root, node_level-1, node)
        else:
            print('None')

    # Aux. method to verify the grandson of a node
    def searchGrandson(self, root, node):
        if root == None:
            return None

        q = []
        q.append(root)

        while (len(q) != 0):
            temp = q.pop(0)
            if temp == node:
                return temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        return None

    # Aux. method to print the grandpas of a node
    def printGrandpas(self, root, level, node):
        if root == None:
            return

        if level == 1:
            if self.searchGrandson(root, node):
                print(root.data)
        elif level > 1:
            self.printGrandpas(root.left, level-1, node)
            self.printGrandpas(root.right, level-1, node)

    # Method to the grandfather of a node
    def findGrandpa(self, root, node):
        if root == None:
            print('None')
            return

        node_level = self.getLevel(root, node)

        if node_level > 2:
            self.printGrandpas(root, node_level - 2, node)
        else:
            print('None')


# Main function
if __name__ == '__main__':

    # Example tree
    binary_tree = BinaryTree("Genisberto Marin")
    binary_tree.root.left = Node("Fernando Marin")
    binary_tree.root.right = Node("Juan Carlos Marin")
    binary_tree.root.left.left = Node("Luis Marin") 
    binary_tree.root.left.right = Node("David Marin") 
    binary_tree.root.right.left = Node("x")
    binary_tree.root.right.right = Node("y")

    binary_tree.inorderTraversal(binary_tree.root)
    print()
    # Preorder traversal
    binary_tree.preorderTraversal(binary_tree.root)
    print()
    # Postorder traversal
    binary_tree.postorderTraversal(binary_tree.root)
    print()

    print('Find uncle(s): ')
    # Get the uncle(s) of a given node
    binary_tree.findUncles(binary_tree.root, binary_tree.root.left.left)

    print('\nFind grandpa: ')
    # Get the grandpa of a given node
    binary_tree.findGrandpa(
        binary_tree.root, binary_tree.root.left.left)
