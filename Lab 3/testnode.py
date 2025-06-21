
from node import Node, TwoWayNode

def printStructure(head):
    """Prints the items in the structure referred to by head."""
    probe = head
    while probe != None:
        print(probe.data, end = " ")
        probe = probe.next
    print()


def makeTwoWay(node):
    """
    Input:
        a head node of a single linked structure

    Output:
        a head node of a two-way linked structure
    """
    if node == None:
        return None

    new_two_way_node = TwoWayNode(node.data)
    previous = new_two_way_node
    current = node.next

    while current != None:
        new_node = TwoWayNode(current.data)
        new_node.previous = previous
        previous.next = new_node
        previous = new_node

        current = current.next

    return new_two_way_node

def main():
    """Tests modifications."""
    head = None

    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)
    
    print("5 4 3 2 1:", end = " ")
    printStructure(head)
    
    print("5 4 3 2 1:", end = " ")
    twoWayHead = makeTwoWay(head)
    printStructure(twoWayHead)


if __name__ == "__main__": 
    main()
