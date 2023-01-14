class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
            if data == self.data:
                return # node already exist

            if data < self.data: #add data in the left subtree  
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = BinarySearchTreeNode(data)
            else: #add data in the right subtree
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
            elements = []

            #visit left tree
            if self.left:
                elements += self.left.in_order_traversal()

            #visit base node
            elements.append(self.data)

            #visit right tree
            if self.right:
                elements += self.right.in_order_traversal()

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
    
def build_tree(elements):
        print("\nBuilding tree with these elements:",elements)
        root = BinarySearchTreeNode(elements[0])

        for i in range(1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__ == '__main__':
        numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
        print("In order traversal gives this sorted list (NUMBERS) :",numbers_tree.in_order_traversal())

        countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
        country_tree = build_tree(countries)
        print("In order traversal gives this sorted list (COUNTRIES) :",country_tree.in_order_traversal())

        print("\nSEARCH METHOD ON BUILD TREE")
        print("Is Philippines in the list? ", country_tree.search("Philippines"))
        print("Is Pakistan is in the list? ", country_tree.search("Pakistan"))