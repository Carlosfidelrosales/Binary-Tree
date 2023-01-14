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

    def measured_sum(self):
        if self.left:
            sum_left = self.left.measured_sum()
        else:
            sum_left = 0
        if self.right:
            sum_right = self.right.measured_sum()
        else:
            sum_right = 0
        return self.data + sum_left + sum_right

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.join_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [12,1,45,24,64,10,33,90]
    letters = ["B", "C", "F", "H", "K", "I"]
    
    numbers_tree = build_tree(numbers)
    letters_tree = build_tree(letters)

    print("\nInput numbers:",numbers)
    print("\nMin:",numbers_tree.obt_min())
    print("\nMax:",numbers_tree.obt_max())
    print("\nSum:", numbers_tree.measured_sum())
    print("\nThe in order traversal:", numbers_tree.inOrder_traversal())
    print("The Pre order traversal:", numbers_tree.preOrder_traversal())
    print("The Post order traversal:", numbers_tree.postOrder_traversal()) 

    print(f"\nInput letters:", letters)
    print(f"\nMin:",letters_tree.obt_min())
    print(f"\nMax:",letters_tree.obt_max())
    print(f"\nThe in order traversal:", letters_tree.inOrder_traversal())
    print(f"The Pre order traversal:", letters_tree.preOrder_traversal())
    print(f"The Post order traversal:", letters_tree.postOrder_traversal()) 