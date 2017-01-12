import random
# For TDD purposes

class Node(object):
    """
    A simple Node object that contains a single int data, and one child Node.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def merge(sll_1, sll_2):
    """
    merge takes two sorted linked lists and returns the merge of two linked list (sorted).
    """
    # Preserve input data
    current_node_sll_1 = sll_1
    current_node_sll_2 = sll_2

    # Check null conditions:
    if sll_1.data is None:
        return sll_2
    if sll_2.data is None:
        return sll_1
    
    # Initialize new Node
    current_head = Node()
    new_head = current_head

    while current_node_sll_1 is not None or current_node_sll_2 is not None:
        # While at least one linked list is not exhausted...
        if current_node_sll_1 is not None and current_node_sll_2 is not None:
            # While both lists are not exhausted...
            # Feed the smallest element of two linkedlists into current_head
            if current_node_sll_1.data <= current_node_sll_2.data:
                current_head.data = current_node_sll_1.data
                current_node_sll_1 = current_node_sll_1.next
            else:
                current_head.data = current_node_sll_2.data
                current_node_sll_2 = current_node_sll_2.next

            # current_head fed, move to the next one
            current_head.next = Node()
            current_head = current_head.next

        elif current_node_sll_1 is None:
            # Linked list 1 exhausted first, attach the rest of linked list 2 to the current node and done.
            current_head.data = current_node_sll_2.data
            current_head.next = current_node_sll_2.next
            break
        else:
            # Linked list 2 exhausted first, attach the rest of linked list 1 to the current node and done.
            current_head.data = current_node_sll_1.data
            current_head.next = current_node_sll_1.next
            break

    return new_head

def create_linked_list(lst):
    """
    The function converts a list to a linked list.
    """
    sll = Node()
    current_node = sll

    for i, x in enumerate(lst):
        current_node.data = x
        if i != len(lst) - 1:
            current_node.next = Node()
            current_node = current_node.next

    return sll

def print_linked_list(ll):
    """
    The function prints out each element of a linked list, for logging purposes.
    """
    while ll != None:
        print(ll.data)
        ll = ll.next

def linked_list_to_list(ll):
    """
    The function convert a linked list to list, for testing purposes.
    """
    result_list = []

    while ll != None:
        result_list.append(ll.data)
        ll = ll.next

    return result_list  

def merge_for_sorted_lists(l1, l2):
    """
    The function merges two sorted lists, for testing purposes.
    """
    return sorted(l1 + l2)

def main():
    # Try 100 test cases:
    for i in range(100):
        # Create two sorted lists with lenth less than 10000, each element less than 100
        l_1 = sorted([int(100 * random.random()) for i in range(int(10000 * random.random()))])
        l_2 = sorted([int(100 * random.random()) for i in range(int(10000 * random.random()))])
        
        # From sorted lists create two sorted linked lists
        sll_1 = create_linked_list(l_1)
        sll_2 = create_linked_list(l_2)

        try:
            # Check the equal length
            assert len(merge_for_sorted_lists(l_1, l_2)) == len(linked_list_to_list(merge(sll_1, sll_2)))
        except AssertionError as e:
            e.args += (l_1, l_2, merge_for_sorted_lists(l_1, l_2), linked_list_to_list(merge(sll_1, sll_2)))
            raise
        try:
            # Check equality
            assert merge_for_sorted_lists(l_1, l_2) == linked_list_to_list(merge(sll_1, sll_2))
        except AssertionError as e:
            e.args += (l_1, l_2, merge_for_sorted_lists(l_1, l_2), linked_list_to_list(merge(sll_1, sll_2)))
            raise
        
    print("All tests passed.")

if __name__ == "__main__":
    main()