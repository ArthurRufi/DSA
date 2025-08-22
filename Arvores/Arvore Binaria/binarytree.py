class RamosDaArvore:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = RamosDaArvore('R')
nodeA = RamosDaArvore('A')
nodeB = RamosDaArvore('B')
nodeC = RamosDaArvore('C')
nodeD = RamosDaArvore('D')
nodeE = RamosDaArvore('E')
nodeF = RamosDaArvore('F')
nodeG = RamosDaArvore('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print("root.right.left.data:", root.right.left.data)