# PAST EXERCISES

# Uncle of a node
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

  binary_tree_ex = BinaryTreeEx(1)             #                 1 //Root Node
  binary_tree_ex.root.left = Node(2)           #                / \
  binary_tree_ex.root.right = Node(3)          #               2   3
  binary_tree_ex.root.left.left = Node(4)      #              / \  / \
  binary_tree_ex.root.left.right = Node(5)     #             4  5  6  7 //Leaf Nodes
  binary_tree_ex.root.right.left = Node(6)     #            /
  binary_tree_ex.root.right.right = Node(7)    #           8
  binary_tree_ex.root.left.left.left = Node(8)

  # Get the level of a given node
  #print(binary_tree_ex.getLevel(binary_tree_ex.root, binary_tree_ex.root.right.right))

  print('Find uncle(s): ')
  # Get the uncle(s) of a given node
  binary_tree_ex.findUncles(binary_tree_ex.root, binary_tree_ex.root.left)

  print('\nFind grandpa: ')
  # Get the grandpa of a given node
  binary_tree_ex.findGrandpa(binary_tree_ex.root, binary_tree_ex.root.left.left.left)

  print('\nFind the max element: ')
  # Get the grandpa of a given node
  binary_tree_ex.printMax(binary_tree_ex.root)

  print('\nFind the min element: ')
  # Get the grandpa of a given node
  binary_tree_ex.printMin(binary_tree_ex.root)

