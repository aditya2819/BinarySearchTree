class Node:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            previousNode = None
            while currentNode:
                previousNode = currentNode
                if currentNode.data > data:
                    currentNode = currentNode.leftNode
                else:
                    currentNode = currentNode.rightNode
            if previousNode.data > data:
                previousNode.leftNode = newNode
            else:
                previousNode.rightNode = newNode

    def search(self, data):
        path = []
        if self.root is None:
            return path
        currentNode = self.root
        while currentNode:
            path.append(currentNode.data)
            if currentNode.data == data:
                return path
            elif currentNode.data > data:
                currentNode = currentNode.leftNode
            else:
                currentNode = currentNode.rightNode
        return []

    def delete(self, data):
        if self.root is None:
            print("Empty Tree")
        else:
            currentNode = self.root
            previousNode = None
            while currentNode:
                if currentNode.data > data:
                    previousNode = currentNode
                    currentNode = currentNode.leftNode
                elif currentNode.data < data:
                    previousNode = currentNode
                    currentNode = currentNode.rightNode
                else:
                    if not currentNode.leftNode and not currentNode.rightNode:
                        if not previousNode:
                            self.root = None
                        elif previousNode.leftNode == currentNode:
                            previousNode.leftNode = None
                        else:
                            previousNode.rightNode = None
                        return
                    elif not currentNode.leftNode:
                        if not previousNode:
                            self.root = currentNode.leftNode
                        elif previousNode.leftNode == currentNode:
                            previousNode.leftNode = currentNode.leftNode
                        else:
                            previousNode.rightNode = currentNode.leftNode
                            return
                    else:
                        previousNextNode = currentNode
                        nextNode = currentNode.rightNode
                        while nextNode.leftNode:
                            previousNextNode = nextNode
                            nextNode = nextNode.leftNode
                        currentNode.data = nextNode.data
                        if previousNextNode == currentNode:
                            previousNextNode.rightNode = nextNode.rightNode
                        else:
                            previousNextNode.leftNode = nextNode.rightNode
                        return

    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.leftNode)
            print(root.data, end=" ")
            self.inOrderTraversal(root.rightNode)

    def preOrderTraversal(self, root):
        if root:
            print(root.data, end=" ")
            self.preOrderTraversal(root.leftNode)
            self.preOrderTraversal(root.rightNode)

    def postOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.leftNode)
            self.postOrderTraversal(root.rightNode)
            print(root.data, end=" ")
