# HTML EXERCISE

# From the statement, I can assume that I already have an dict of html elements.
HTML_tags = {'html':['head','body'], 'head':['title'], 'body':['header', 'nav', 'article', 'footer'], 'nav':['ul'], 'article':['h1', 'p'], 'ul':['li', 'li', 'li']}

# Node class (tag)
class Tag:

  def __init__(self, name, children_count = 0):
    self.name = name
    self.children = []
    self.children_count = children_count

# WebTree class
class WebTree:

  def __init__(self):
    self.root = Tag('html')
    self.root.children_count = 1
  
  # Method to add a new tag to another tag
  def addTag(self, tag, name):
    temp = Tag(name)
    tag.children.append(temp)
    tag.children_count += 1
  
  # Method to traverse the entire tree
  def levelOrderTraversal(self, root):
    if root == None:
      return

    q = []
    q.append(root)
    while len(q):
      n = len(q)
      while n > 0:
        temp = q.pop(0)
        print(temp.name, end=' ')

        for i in range(len(temp.children)):
          q.append(temp.children[i])
        n = n - 1
      
      print()
  
  # Method to search a tag
  def search(self, root, name):
    if root == None:
      return None

    q = []
    q.append(root)
    while len(q):
      n = len(q)
      while n > 0:
        temp = q.pop(0)
        if temp.name == name:
          return temp

        for i in range(len(temp.children)):
          q.append(temp.children[i])
        n = n - 1
    
    return None

if __name__ == '__main__':
  # New tree
  html_tree = WebTree()

  # Traversal before adding tags
  print('Traversal before adding tags:')
  html_tree.levelOrderTraversal(html_tree.root)

  # Iterating through all the dict. with html elements
  for parent in HTML_tags:

    element = html_tree.search(html_tree.root, parent)  # Looking for the tag on the tree

    if element:   # To avoid repeating tags.
      for children in HTML_tags[parent]:
        html_tree.addTag(element, children)   # Adding each pair (parent tag, child tag)
  

  # Traversal after adding tags
  print('\nTraversal after adding tags:')
  html_tree.levelOrderTraversal(html_tree.root)
