import queue

# Generic Tree Class
class GenericTreeNode:
    def __init__(self, data):
        self.data: int = data
        self.children: list = []

 
# Take Level Wise Input By Entering Each Data
def take_level_wise_input_via_each_data():
    """
    Takes a user input for each node and create a Generic Tree step by step and return root of that tree.
    """
    
    # Create a Queue to hold nodes 
    q: queue.Queue = queue.Queue()

    # Take root data input
    root_data: int = int(input("Enter Root Data: "))
    
    # Create Root Node from root_data
    root: GenericTreeNode = GenericTreeNode(root_data)

    # Enque root node in queue
    q.put(root)

    # Iterate till Queue is not Empty
    while not q.empty():
        # Deque from queue
        curr_node: GenericTreeNode = q.get()
        
        # Take Children count for current node
        children_count: int = int(input(f"Enter Number of Children for {curr_node.data}: "))
        
        # Take each child data and create node
        for _ in range(children_count):
            # Enter Child Data
            child_data = int(input(f"Enter Child Data of {curr_node.data}: "))
            child_node: GenericTreeNode = GenericTreeNode(child_data)
            q.put(child_node)
            curr_node.children.append(child_node)

    return root


# Creates a Generic Tree from a user input list
def take_level_wise_input_via_single_list(li: list) -> None:
    """
    Takes a list and create a Generic Tree and return root of that tree.
    Format of List: [rootData, NoOfChildren_2, childData, ChildData, NoOfChildren_1, ChildData, 0]
    """
    if len(li) == 0:
        return None
    
    q: queue.Queue = queue.Queue()

    i: int = 0

    root: GenericTreeNode = GenericTreeNode(li[i])

    i += 1

    q.put(root)

    while not q.empty():
        curr_node: GenericTreeNode = q.get()
        children_count: int= li[i]
        i += 1
        for j in range(i, i+children_count):
            child_node: GenericTreeNode = GenericTreeNode(li[j])
            q.put(child_node)
            curr_node.children.append(child_node)

        i += children_count

    return root

# Root: Child Relation type printing
def print_tree_detailed(root: GenericTreeNode) -> None:
    if root.data is None:
        return

    print(f"{root.data}:", end="")

    for node in root.children:
        if node is not None:
            print(node.data, end=",")
    
    print()

    for node in root.children:
        print_tree_detailed(node)


# Print Tree Level Wise 
def print_level_wise(root: GenericTreeNode) -> None:
    # If Tree is empty
    if root is None:
        return

    # Create queue
    q = queue.Queue()

    # Enque root node in queue
    q.put(root)

    # Iterate till queue is not empty
    while not q.empty():
        # Deque from queue
        current_node = q.get()

        child_li = []

        # Traverse current not children and enque in queue
        for child in current_node.children:
            child_li.append(str(child.data))
            q.put(child)
        
        # Print Parent:Children without trailing extra comma
        child_li_str = ",".join(child_li)
        print(f"{current_node.data}:{child_li_str}")
