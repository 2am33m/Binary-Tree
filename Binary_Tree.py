class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left: 
                self.left.add_child(data)
            else:
                self.left = Node(data)
            
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Node(data)


    def in_order_traversal(self):
        elements = []
        # Visit left node trees first 

        if self.left: 
            elements += self.left.in_order_traversal()

        # Visit base node

        elements.append(self.data)

        # Visit right node

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False    

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False    

        
def build_tree(elements):
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [22, 18, 21, 20, 10, 11]

    tree = build_tree(numbers)

    print(tree.search(21))






