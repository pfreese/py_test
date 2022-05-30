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

numTree = to_binary_tree([1, 2, 3, 4, 5, 6, 7])
numBFS = [1, 2, 3, 4, 5, 6, 7]
numDFS = [1, 2, 4, 5, 3, 6, 7]

# Alphabetical.
alphaTree = to_binary_tree(["A", "B", "C", "D", None, "E", "F", None, None, None, None, "G", "H", "I", None])
alphaBFS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
alphaDFS = ["A", "B", "D", "C", "E", "G", "H", "F", "I"]
