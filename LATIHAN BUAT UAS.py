class TreeNode :
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children :
            ret += child.__str__(level + 1)
        return ret

    def addChild (self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Transportasi',[])
darat = TreeNode ('Darat',[])
laut = TreeNode ('Laut',[])
udara = TreeNode ('darat',[])
tree.addChild(darat)
tree.addChild(laut)
tree.addChild(udara)
dua = TreeNode ('Roda 2',[])
empat = TreeNode ('Roda 4',[])
darat.addChild(dua)
darat.addChild(empat)
kend1 = TreeNode('Motor',[])
kend2 = TreeNode('Sepeda',[])
kend3 = TreeNode('Mobil',[])
dua.addChild(kend1)
dua.addChild(kend2)
empat.addChild(kend3)
kend4 = TreeNode('Kapal',[])
kend5 = TreeNode('Pesawat',[])
laut.addChild(kend4)
udara.addChild(kend5)
print(tree)
