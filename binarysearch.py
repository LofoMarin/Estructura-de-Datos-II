###### BINARY SEARCH TREE ######

# CLASS: NODE
class BST_Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

# CLASS: BINARY SEARCH TREE
class BSTree:
  def __init__(self, root_data = 0):
    self.root = BST_Node(root_data)

  # Level order traversal
  def levelOrderTraversal(self, root):
    if root == None:
      return

    q = []
    q.append(root)
    while len(q):
      temp = q.pop(0)
      print(temp.data, end = ' ')

      if temp.left:
        q.append(temp.left)
      
      if temp.right:
        q.append(temp.right)
  
  # Method to search in the BSTree
  def search(self, root, data):
    if root == None:
      return

    if root.data == data:
      return root
    
    if data < root.data:
      return self.search(root.left, data)
    else:
      return self.search(root.right, data)

  # Method to insert a node
  def insert(self, root, data):
    if root == None:
      root = BST_Node(data)
    
    q = []
    q.append(root)
    while len(q):
      temp = q.pop(0)

      if temp.data > data:
        if (temp.left == None):
          temp.left = BST_Node(data)
        else:
          q.append(temp.left)

      if temp.data < data:
        if (temp.right == None):
          temp.right = BST_Node(data)
        else:
          q.append(temp.right)

  # Aux. method to delete a node (return list inorder traversal)
  def listInorderElement(self, root, inorderList):
    if root == None:
      return
    
    self.nextInorderElement(root.left)
    inorderList.append(root)
    self.nextInorderElement(root.right)

  # Aux. method to find min. value
  def minValueNode(self, node):
    current = node
  
    while(current.left is not None):
        current = current.left
  
    return current

  # Method to delete a node
  def delete(self, root, key):
  
    if root == None:
        return root
  
    if key < root.data:
        root.left = self.delete(root.left, key)
    elif(key > root.data):
        root.right = self.delete(root.right, key)
    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
  
        temp = self.minValueNode(root.right)
        root.data = temp.data
        root.right = self.delete(root.right, temp.data)
  
    return root




if __name__ == '__main__':

  # Example tree

  binary_search_tree = BSTree(10)             #                 10 //Root Node

  # Search
  print(binary_search_tree.search(binary_search_tree.root, 2))

  # Insert
  binary_search_tree.insert(binary_search_tree.root, 2)

  # Level order traversal
  binary_search_tree.levelOrderTraversal(binary_search_tree.root)
  print()

  # Delete
  binary_search_tree.delete(binary_search_tree.root, 2)

  # Level order traversal
  binary_search_tree.levelOrderTraversal(binary_search_tree.root)
  print()
  
