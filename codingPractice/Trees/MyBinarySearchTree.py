from codingPractice.Trees.MyBinaryTree import *


def insert(root, node):
    if root is None:
        return MyNode(node)
    if root.value > node:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root


def delete(root, node_to_delete):
    # Base Case:
    if root is None:
        return root
    if root.value > node_to_delete:
        root.left = delete(root.left, node_to_delete)
    elif root.value < node_to_delete:
        root.right = delete(root.right, node_to_delete)
    else:
        # if its not greater than or less than we can assume its equal to the node we want to delete
        # Case 1: node_to_delete is a leaf node
        # Case 2: node_to_delete has 1 child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            # Case 3: node_to_delete has 2 children
                # get in order successor of the node (smallest successor of the current node, i.e keep going left)
                # swap with the node_to_delete
                # delete the in order successor
            successor = get_min_value_node(root.right)
            root.value = successor.value
            root.right = delete(root.right, successor.value)

    return root


def get_min_value_node(node):
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node


def main():
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)
    root.print_in_order()
    root = delete(root, 6)
    print("\nAfter Deletion")
    root.print_in_order()


if __name__ == '__main__':
    main()

