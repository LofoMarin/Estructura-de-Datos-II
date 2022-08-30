###### SIMPLE BINARY TREE ######

# CLASS: NODE
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# CLASS: BINARY TREE


class BinaryTree:
    def __init__(self, root_data=0):
        self.root = Node(root_data)

    # AUXILIARY OPERATIONS

    # Method to get the level of a node
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

    # Method to get the height of the tree

    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    # Method to print the nodes on the current level
    def printCurrentLevel(self, root, level):
        if root == None:
            return

        if level == 1:
            print(root.data, end=' ')
        elif level > 1:
            self.printCurrentLevel(root.left, level-1)
            self.printCurrentLevel(root.right, level-1)

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

    # Method to print level order traversal
    def levelOrderTraversal(self, node):
        h = self.height(node)
        for i in range(1, h+1):
            self.printCurrentLevel(node, i)

    # BASIC OPERATIONS

    # Method to insert a new node
    def insert(self, root, data):
        if root == None:
            return

        q = []
        q.append(root)

        while (len(q) != 0):
            temp = q[0]
            q.pop(0)

            if (temp.left == None):
                temp.left = Node(data)
                break
            else:
                q.append(temp.left)

            if (temp.right == None):
                temp.right = Node(data)
                break
            else:
                q.append(temp.right)

    # Aux. method to delete a node
    def deleteDeepest(self, root, d_node):
        q = []
        q.append(root)
        while (len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def delete(self, root, data):
        if root == None:
            return None
        if root.left == None and root.right == None:
            if root.data == data:
                return None
            else:
                return root

        data_node = None
        q = []
        q.append(root)
        temp = None

        while (len(q) != 0):
            temp = q.pop(0)
            if temp.data == data:
                data_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        if data_node != None:
            x = temp.data
            self.deleteDeepest(root, temp)
            data_node.data = x
        return root

    # Method to search a node
    def search(self, root, data):
        if root == None:
            return

        q = []
        q.append(root)

        while (len(q) != 0):
            temp = q.pop(0)
            if temp.data == data:
                print('YES')
                return
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        print('NO')
        return

    # Method to check if it is full binary:
    def checkFull(self, root):
        if root == None:
            return True

        q = []
        q.append(root)

        while len(q):
            temp = q.pop(0)

            if (temp.left != None and temp.right == None) or (temp.left == None and temp.right != None):
                return False

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        return True

    # Method to check if it is complete binary:
    def checkComplete(self, root):
        if root == None:
            return True

        q = []
        q.append(root)

        sw = False

        while len(q):
            temp = q.pop(0)

            if temp.left:
                if sw == True:
                    return False
                q.append(temp.left)
            else:
                sw = True

            if temp.right:
                if sw == True:
                    return False
                q.append(temp.right)
            else:
                sw = True

        return True

    # Method to check if it is perfect binary:
    def checkPerfect(self, root):
        if root == None:
            return True

        q = []
        q.append(root)
        count = 0

        while len(q):
            temp = q.pop(0)

            if (temp.left == None and temp.right == None) or (temp.left != None and temp.right != None):
                count = count + 1
            else:
                return False

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        if (2 ** self.height(root) - 1) == count:
            return True
        else:
            return False


# Main function
if __name__ == '__main__':

    print('Testing on Binary Tree #1:\n')

    # Example tree
    binary_tree = BinaryTree(1)  # 1 //Root Node
    binary_tree.root.left = Node(2)  # / \
    binary_tree.root.right = Node(3)  # 2   3
    binary_tree.root.left.left = Node(4)  # / \  / \
    binary_tree.root.left.right = Node(5)  # 4  5  6  7 //Leaf Nodes
    binary_tree.root.right.left = Node(6)
    binary_tree.root.right.right = Node(7)

    # Inorder traversal
    binary_tree.inorderTraversal(binary_tree.root)
    print()
    # Preorder traversal
    binary_tree.preorderTraversal(binary_tree.root)
    print()
    # Postorder traversal
    binary_tree.postorderTraversal(binary_tree.root)
    print()
    # Height of the tree
    print(binary_tree.height(binary_tree.root))
    # Print the current level
    binary_tree.printCurrentLevel(binary_tree.root, 2)
    print()
    # Level order traversal
    binary_tree.levelOrderTraversal(binary_tree.root)
    print()

    # Insert new node
    binary_tree.insert(binary_tree.root, 2)
    # Level order traversal
    binary_tree.levelOrderTraversal(binary_tree.root)
    print()

    # Delete a node
    binary_tree.delete(binary_tree.root, 5)
    # Level order traversal
    binary_tree.levelOrderTraversal(binary_tree.root)
    print()

    # Search a node
    binary_tree.search(binary_tree.root, 5)

    # Check whether the tree is full or not
    print(binary_tree.checkFull(binary_tree.root))
    # Insert new node
    binary_tree.insert(binary_tree.root, 11)
    # Check whether the tree is full or not
    print(binary_tree.checkFull(binary_tree.root))

    # Check whether the tree is complete or not
    print(binary_tree.checkComplete(binary_tree.root))

    print('\nTesting on Binary Tree #2:\n')

    # Another example tree

    binary_tree_2 = BinaryTree(1)  # 1 //Root Node
    binary_tree_2.root.left = Node(2)  # / \
    binary_tree_2.root.right = Node(3)  # 2   3

    # Check whether the tree is complete or not
    print(binary_tree_2.checkComplete(binary_tree_2.root))

    # Check whether the tree is perfect or not
    print(binary_tree_2.checkPerfect(binary_tree_2.root))

    print('\nTesting on Binary Tree #3:\n')

    # Another example tree
    binary_tree_3 = BinaryTree(1)  # 1 //Root Node
    binary_tree_3.root.left = Node(2)  # / \
    binary_tree_3.root.right = Node(3)  # 2   3
    binary_tree_3.root.left.left = Node(4)  # / \  / \
    binary_tree_3.root.left.right = Node(5)  # 4  5  6  7 //Leaf Nodes
    binary_tree_3.root.right.left = Node(6)
    binary_tree_3.root.right.right = Node(7)

    # Check whether the tree is perfect or not
    print(binary_tree_3.checkPerfect(binary_tree_3.root))




# ------------------------------------------------------------------------------------------------------------
class BinaryTreeEx(BinaryTree):

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

    # Method to print the MAX. value of a binary tree
    def printMax(self, root):
        if root == None:
            return

        q = []
        q.append(root)
        max = root
        while len(q):
            temp = q.pop(0)
            if temp.data > max.data:
                max = temp

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        print(f'{max.data} in level {self.getLevel(root, max)}')

    # Method to print the MAX. value of a binary tree
    def printMin(self, root):
        if root == None:
            return

        q = []
        q.append(root)
        min = root
        while len(q):
            temp = q.pop(0)
            if temp.data < min.data:
                min = temp

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        print(f'{min.data} in level {self.getLevel(root, min)}')


if __name__ == '__main__':

    # Tree to use for exercises

    binary_tree_ex = BinaryTreeEx(1)  # 1 //Root Node
    binary_tree_ex.root.left = Node(2)  # / \
    binary_tree_ex.root.right = Node(3)  # 2   3
    binary_tree_ex.root.left.left = Node(4)  # / \  / \
    binary_tree_ex.root.left.right = Node(5)  # 4  5  6  7 //Leaf Nodes
    binary_tree_ex.root.right.left = Node(6)  # /
    binary_tree_ex.root.right.right = Node(7)  # 8
    binary_tree_ex.root.left.left.left = Node(8)

    # Get the level of a given node
    #print(binary_tree_ex.getLevel(binary_tree_ex.root, binary_tree_ex.root.right.right))

    print('Find uncle(s): ')
    # Get the uncle(s) of a given node
    binary_tree_ex.findUncles(binary_tree_ex.root, binary_tree_ex.root.left)

    print('\nFind grandpa: ')
    # Get the grandpa of a given node
    binary_tree_ex.findGrandpa(
        binary_tree_ex.root, binary_tree_ex.root.left.left.left)

    print('\nFind the max element: ')
    # Get the grandpa of a given node
    binary_tree_ex.printMax(binary_tree_ex.root)

    print('\nFind the min element: ')
    # Get the grandpa of a given node
    binary_tree_ex.printMin(binary_tree_ex.root)
