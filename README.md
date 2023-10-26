# Binary Search Tree (BST) Python Implementation

This Python code provides an implementation of a Binary Search Tree (BST) and demonstrates various operations on it. A BST is a data structure that organizes data elements in a tree-like structure, where each node has at most two children. The elements in the tree are arranged such that for any given node:

- All elements in the left subtree are smaller or equal to the node's value.
- All elements in the right subtree are greater.

## Features

The provided code includes the following features and operations:

1. **BST Node Class**:
   - The `Node` class represents a single node in the BST. It contains data, a reference to the left child, and a reference to the right child.

2. **Binary Search Tree (BST) Class**:
   - The `BinarySearchTree` class represents the BST. It contains the root node and supports the following operations:
     - **Insertion**: Add a new element to the tree while maintaining the BST property.
     - **In-Order Traversal**: Print the elements of the tree in ascending order.
     - **Pre-Order Traversal**: Print the elements in pre-order (root, left, right) fashion.
     - **Post-Order Traversal**: Print the elements in post-order (left, right, root) fashion.
     - **Search**: Find an element in the tree and return the path taken during the search.
     - **Deletion**: Remove a specific element from the tree while maintaining the BST property.

## Usage

You can use this code to create a Binary Search Tree, insert elements, and perform various operations.

# Example test cases and expected outputs are provided in the test.py code.
