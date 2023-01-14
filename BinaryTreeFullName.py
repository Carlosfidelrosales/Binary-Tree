# Create a demo using the letters in your fullname as the content of the binary tree.
# Upload all source code in new github repository.

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inOrder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrder_traversal()

        return elements

    def postOrder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrder_traversal()
        if self.right:
            elements += self.right.postOrder_traversal()

        elements.append(self.data)

        return elements

    def preOrder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preOrder_traversal()
        if self.right:
            elements += self.right.preOrder_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def obt_max(self):
        if self.right is None:
            return self.data
        return self.right.obt_max()

    def obt_min(self):
        if self.left is None:
            return self.data
        return self.left.obt_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.obt_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    alphabets = ["C", "A", "R", "L", "O", "S", "F", "I", "D", "E", "L", "R", "O", "S", "A", "L", "E", "S"]
    alphabets_tree = build_tree(alphabets)


    print(f"\nInput letters:", alphabets)

    print(f"\nTHE MINUMUM AND MAXIMUM VALUE OF ELEMENT/LETTER THAT IS PRESENT IN THE FULL NAME.")
    print(f"   Min:", alphabets_tree.obt_min())
    print(f"   Max:", alphabets_tree.obt_max())

    print(f"\nBY BINARY TREE TRAVERSALS,")
    print(f"   The In order traversal:", alphabets_tree.inOrder_traversal())
    print(f"   The Pre order traversal:", alphabets_tree.preOrder_traversal())
    print(f"   The Post order traversal:", alphabets_tree.postOrder_traversal())

    print(f"\nBY DELETING AN ALPHABET,")
    # alphabets_tree.delete("R")
    # print("   After removing the letter R ", alphabets_tree.inOrder_traversal())
    alphabets_tree.delete("A")
    print("   After removing the letter A ", alphabets_tree.inOrder_traversal())
    
    print(f"\nBY SEARCHING ON BUILD TREE,")
    print("   Is Letter O located on the list? ", alphabets_tree.search("O"))
    print("   Is Letter Z located on the list? ", alphabets_tree.search("Z"))
