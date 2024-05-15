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
            

    def find_min(self):
        if self.left is None: 
            return self.data    
        else:
           return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
        

    def calculate_sum(self):
        sum = self.data

        # Sum left nodes 
        if self.left:
            sum += self.left.calculate_sum()

        # Sum base node
        sum += self.data

        # Sum right nodes 
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def post_order_traversal(self):
        elements = []

        # Visit the left nodes first 
        if self.left: 
            elements += self.left.post_order_traversal()

        # Vists the right nodes     
        if self.right:
            elements += self.right.post_order_traversal()

        #add the root node
        elements.append(self.data)
        
        return elements
    
    def pre_order_traversal(self):
        elements = []

        # Visit the root node first
        elements.append(self.data)

        #Visit the left node first
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements    

def build_tree(elements):
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers = [22, 18, 21, 20, 10, 11]

    tree = build_tree(numbers)

    print(tree.calculate_sum())






