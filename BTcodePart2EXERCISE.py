# Modify delete method in class BinarySearchTreeNode class to use min element from left subtree. You will remove lines marked with ---> and use max value from left subtree

#     def delete(self, val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
#         else:
#             if self.left is None and self.right is None:
#                 return None
#             elif self.left is None:
#                 return self.right
#             elif self.right is None:
#                 return self.right

#           --->  min_val = self.right.find_min()
#           --->  self.data = min_val
#           --->  self.right = self.right.delete(min_val)

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

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.join_child(elements[i])

    return root
    
if __name__ == '__main__':
    numbers = [45, 4, 7, 12, 9, 61, 10, 74]
    numbers_tree = build_tree(numbers)

    # numbers_tree.delete(7)
    # print("After removing the number 7 ", numbers_tree.inOrder_traversal()) 
    # numbers_tree.delete(10)
    # print("After removing the number 10 ", numbers_tree.inOrder_traversal()) 
    # numbers_tree.delete(61)
    # print("After removing the number 61 ", numbers_tree.inOrder_traversal())