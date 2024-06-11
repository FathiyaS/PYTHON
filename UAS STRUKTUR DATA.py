class TreeNode:
    def _init__(self, data, children=[]):
        self.data = data
        self.children = children
        
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child. _str_(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        
tree = TreeNode('Kakek', [])
anak1 = TreeNode('Anak Pertama', [])
anak2 = TreeNode ('Anak Kedua', [])
anak3 = TreeNode('Anak Ketiga',[])
tree.addChild(anak1)
tree.addChild(anak2)
tree.addChild(anak3)
print (tree)
