
class Node:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self,key):

           if key < self.key:
               if self.left is None:
                  self.left = Node(key)
               else:
                  self.left.insert(key)

           elif key > self.key:
               if self.right is None:
                  self.right = Node(key)
               else:
                  self.right.insert(key)

    def search(self,key):

         if self.key is None:
                return

         if self.key == key:
                return self.key

         if key > self.key:
             if self.right:
                 return  self.right.search(key)

         if key < self.key:
             if self.left:
                return self.left.search(key)


    def printTreeInOrder(self):
        if self.left:
             self.left.printTreeInOrder()
        print(self.key, end=', ')
        if self.right:
             self.right.printTreeInOrder()

    def printTreePreOrder(self):
        if self.key:
            print(self.key,end=', ')
        if self.left:
             self.left.printTreePreOrder()
        if self.right:
            self.right.printTreePreOrder()

    def printTreePostOrder(self):
        if self.left:
             self.left.printTreePostOrder()
        if self.right:
             self.right.printTreePostOrder()
        print(self.key, end=', ')


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print("Pre Order:")
root.printTreePreOrder()
print("\nIn Order")
root.printTreeInOrder()
print("\nPost Order")
root.printTreePostOrder()
print()

print(root.search(19))




