class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# From: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion to build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()

simpTree = to_binary_tree([1, 2, 3, None, None, 4, 5])
complexTree = to_binary_tree([3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14])
