class TreeNode :
    def __init__(self, val):
        self.leftChild = None
        self.rightChild = None
        self.data = val

def preOrderTraversal(root_node) :
    if root_node:
        print(root_node.data, end = '')
        preOrderTraversal(root_node.leftChild)
        preOrderTraversal(root_node.rightChild)

def inOrderTraversal(root_node) :
    if root_node:
        inOrderTraversal(root_node.leftChild)
        print(root_node.data, end = '')
        inOrderTraversal(root_node.rightChild)

def postOrderTraversal(root_node) :
    if root_node:
        postOrderTraversal(root_node.leftChild)
        postOrderTraversal(root_node.rightChild)
        print(root_node.data, end = '')

newTree = TreeNode("Drinks")
newTree.leftChild = TreeNode("Hot")
newTree.leftChild.leftChild = TreeNode("Latte")
newTree.leftChild.rightChild = TreeNode("Mocca")
newTree.rightChild = TreeNode("Cold")
newTree.rightChild.leftChild = TreeNode("Coke")
newTree.rightChild.rightChild = TreeNode("Sprite")

print("preOrderTraversal")
print (preOrderTraversal(newTree))
print("")
print("inOrderTraversal")
inOrderTraversal(newTree)
print("")
print("postOrderTraversal")
postOrderTraversal(newTree)
print("")
