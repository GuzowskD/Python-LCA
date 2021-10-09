from BinaryTree import BinaryTree

def readFile(filename):
    try:
        file = open(filename, "r")
        lines = file.read().splitlines()
        file.close()
        return lines
    except:
        print("File not found or could not be opened.")
        return []
    
def main():
    filepath = input("Enter the location of the input file: ")
    if len(filepath) > 0:
        list = readFile(filepath)
    else:
        list = readFile("./input.txt")

    bt = BinaryTree(list)
    if bt.getSize() == 0:
        print("Tree could not be constructed.")
        return
    bt.print()
    print("Type 'exit' to close the program at any time.")
    userCommand = ""
    while userCommand != "exit":
        userCommand = input("Enter your 2 values, separated by a colon ':' > ")
        if userCommand != "exit":
            values = userCommand.split(":")
            if len(values) == 2 and len(values[0]) > 0 and len(values[1]) > 0:
                print("LCA(" + values[0] + ", " + values[1] + ") = " + bt.LCA(values[0], values[1]) + ".\n")
            else:
                print("Error: Expected 2 values separated by a colon.")
    print("Program finished.")



if __name__ == "__main__":
    main()