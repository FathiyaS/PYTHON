class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data

   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

   def inorderTraversal(self, root):
      res = []
      if root:
         res = res + self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res
   def PostorderTraversal(self, root):
       res = []
       if root:
           res = res + self.PostorderTraversal(root.left)
           res = res + self.PostorderTraversal(root.right)
           res.append(root.data)
       return res
         
root = Node(13)
root.insert(8)
root.insert(12)
root.insert(4)
root.insert(3)
root.insert(2)
root.insert(28)
root.insert(40)
print ("inOrder")
print(root.inorderTraversal(root))
print ("")
print ("PreOrder")
print(root.PreorderTraversal(root))
print ("")
print ("PostOrder")
print(root.PostorderTraversal(root)) 
