# PART 1 EXERCISE:

# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. inOrder_traversal(): performs post order traversal of a binary tree
# 5. preOrder_traversal(): perofrms pre order traversal of a binary tree
    
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def join_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.join_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.join_child(data)
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
    




        