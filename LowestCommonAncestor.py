from os import read
from BinaryTree import BinaryTree

def readFile(filename):
    file = open(filename, "r")
    lines = file.read().splitlines()
    file.close()
    return lines
    

def main():
    list = readFile("./input.txt")
    for i in range(len(list)):
        list[i].replace("\n", "")

    bt = BinaryTree(list)
    bt.print()
    lca = bt.LCA("H", "D")
    print("LCA: " + lca)
    lca = bt.LCA("S", "M")
    print("LCA: " + lca)
    lca = bt.LCA("K", "Z")
    print("LCA: " + lca)



if __name__ == "__main__":
    main()