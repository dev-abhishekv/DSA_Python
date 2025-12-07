from tree_operations_module import BinaryTreeNode

class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    #  Print Tree Helper Function
    def __helper_print_tree(self, root):
        if root is None:
            return None
        
        print(f"{root.data}:", end="")

        if root.left:
            print(f"L:{root.left.data},", end="")
        
        if root.right:
            print(f"R:{root.right.data}", end="")
        
        print()

        self.__helper_print_tree(root.left)
        self.__helper_print_tree(root.right)


    # Search Tree Helper Function
    def __helper_search(self, root, data):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        if root.data > data:
            return self.__helper_search(root.left, data)
        else:
            return self.__helper_search(root.right, data)

    #  Insert Into Tree Helper Function
    def __helper_insert(self, root, data):
        if root is None:
            newNode = BinaryTreeNode(data)
            root = newNode
            return root
        
        if root.data >= data:
            new_link = self.__helper_insert(root.left, data)
            root.left = new_link
            return root

        if root.data < data:
            new_link = self.__helper_insert(root.right, data)
            root.right = new_link    
            return root

    # Finds and return minimum element of Node
    def __find_min_node(self, root):
        if root is None:
            return float("inf")

        if root.left is None:
            return root.data

        return self.__find_min_node(root.left)
    

    # Delete From Tree Helper Function
    def __helper_delete(self, root, data):
        # If the tree is empty we can't delete anything 
        if root is None:
            return False, None
        
        # If data is > root means its on right side so call on right
        if data > root.data:
            deleted, new_right = self.__helper_delete(root.right, data)
            root.right = new_right
            return deleted, root
        
        # If data is < root means its on the left side so call on left
        if data < root.data:
            deleted, new_left = self.__helper_delete(root.left, data)
            root.left = new_left
            return deleted, root
        
        # If above cases not satisfied means root.data == data and we need to
        # Delete the root, we have three cases now

        # 1) Root is the leaf Node
        if root.left is None and root.right is None:
            return True, None
        # 2) Root is having one child
        elif root.left is None:
            return True, root.right
        elif root.right is None:
            return True, root.left
        # 3) Root is having 2 children
        # We promote right side min as root data and call delete on right side with the promoted data
        else:
            min_right_data = self.__find_min_node(root.right)
            root.data = min_right_data
            deleted, new_right = self.__helper_delete(root.right, min_right_data)
            root.right = new_right
            return deleted, root


    # Print Tree Base Function
    def printTree(self):
        self.__helper_print_tree(self.root)
    
    # Search Tree Base Function
    def search(self, data):
        return self.__helper_search(self.root, data)

    # Insert into Tree Base Function
    def insert(self, data):
        self.numNodes += 1
        self.root = self.__helper_insert(self.root, data)
    
    # Delete From Tree Base Function
    def delete(self, data):
        deleted, self.root = self.__helper_delete(self.root, data)
        if deleted:
            self.numNodes -= 1
        
        return deleted

    # Count Node in Base Tree Function
    def count(self):
        return self.numNodes
        
b = BST()
q = "Y"
while (q == "y" or q == "Y"):
    print("1: Insert \n2: Delete \n3: Search \n4: Node Count \nOthers: Display \n")
    
    choice = int(input("Enter Choice: "))

    if choice == 1:
        data = int(input("Enter Data: "))
        b.insert(data)
    elif choice == 2:
        data = int(input("Enter Data: "))
        print(f"Node Deleted: {b.delete(data)}")
    elif choice == 3:
        data = int(input("Enter Data: "))
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    elif choice == 4:
        print(f"Number of Nodes: {b.count()}")
    else:
        b.printTree()
    
    q = input("Do You Want More Operations: Y/N: ")