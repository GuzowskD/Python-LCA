
class BinaryTreeNode:
    value = None
    left = None
    right = None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    root = None
    size = 0
    def add(self, value):
        if value == None:
            return
        node = self.root
        while(True):
            if(node.value == value):
                print("Duplicate value: " + str(value))
                return
            
            if(node.value > value):
                if(node.left == None):
                    node.left = BinaryTreeNode(value)
                    self.size += 1
                    return
                else:
                    node = node.left

            else:
                if(node.right == None):
                    node.right = BinaryTreeNode(value)
                    self.size += 1
                    return
                else:
                    node = node.right  

 
    def __init__(self, inputArray):
        if inputArray == None:
            return
        if len(inputArray) == 0:
            return
        self.root = BinaryTreeNode(inputArray[0])
        self.size = 1
        i = 1
        while i < len(inputArray):
            self.add(inputArray[i])
            i += 1

    def search(self, node, value, path):
        if(node == None):
            return None
        if(path != None):
            path.append(node.value)
        
        if(node.value == value):
            return node
        elif(node.value > value):
            return self.search(node.left, value, path)
        else:
            return self.search(node.right, value, path)

    def printTree(self, node, prefix):
        if(node == None):
            return prefix + "-None\n"
        return prefix + "-" + str(node.value) + "\n" + self.printTree(node.right, prefix + " |") + self.printTree(node.left, prefix + "  ")

    def getSize(self):
        return self.size

    def shape(self):
        return self.printTree(self.root, "")

    def print(self):
        print(self.printTree(self.root, ""))

    def LCA(self, value1, value2):
        if value1 == None or value2 == None:
            return "None"
        path1 = []
        path2 = []
        node1 = self.search(self.root, value1, path1)
        node2 = self.search(self.root, value2, path2)

        if(node1 == None):
            print(str(value1) + " does not exist in the tree!")
            return "None"
        if(node2 == None):
            print(str(value2) + " does not exist in the tree!")
            return "None"
        if(node1 == node2):
            return node1.value # Values were identical

        length = len(path1)
        for i in range(length):
            if not path1[i] in path2:
                return path1[i - 1]
        
        return node1.value #Path 1 was shorter -> LCA = last value of Path 1

    