import bst

# Create a BinarySearchTree object
bst = bst.BinarySearchTree()

# Test 1: Insertion
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Test 2: In-Order Traversal
print("In-Order Traversal:")
bst.inOrderTraversal(bst.root)  # Expected output: 20 30 40 50 60 70 80

# Test 3: Pre-Order Traversal
print("\nPre-Order Traversal:")
bst.preOrderTraversal(bst.root)  # Expected output: 50 30 20 40 70 60 80

# Test 4: Post-Order Traversal
print("\nPost-Order Traversal:")
bst.postOrderTraversal(bst.root)  # Expected output: 20 40 30 60 80 70 50

# Test 5: Searching
search_value = 60
path = bst.search(search_value)
print(f"\nSearch for {search_value}:")
print("Path:", path)  # Expected output: Path: [50, 70, 60]

# Test 6: Deletion
delete_value = 30
bst.delete(delete_value)
print(f"\nDelete {delete_value} and In-Order Traversal:")
bst.inOrderTraversal(bst.root)  # Expected output: 20 40 50 60 70 80
