class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        node = Node(new_val)
        if(self.root):
            current = self.root
            parent = None
            while(current !=None):
                parent = current
                if(new_val < current.value):
                    current = current.left
                else:
                    current = current.right
            if(new_val < parent.value):
                parent.left = node
            else:
                parent.right = node
        else:
            self.root = node
        return self.root

    def printSelf(self):
        # Your code goes here
        print( self.root.value )
        return self.root
        
    def search(self, find_val):
        # Your code goes here
        while self.root != None:
            if self.root.value == find_val:
                return True
            elif self.root.value < find_val:
                self.root = self.root.right
            elif self.root.value > find_val:
                self.root = self.root.left
        return False

tree = BST(4)

tree.printSelf().value
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.search(-1))