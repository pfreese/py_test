# Make TreeNode class.
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# From: https://stackoverflow.com/questions/43097045/best-way-to-construct-a-binary-tree-from-a-list-in-python
def to_binary_tree(items: list) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def build(i):
        if i >= n or items[i] is None:
            return None
        node = TreeNode(items[i])
        node.left = build((2*i) + 1)
        node.right = build((2*i) + 2)

        return node
    return build(0)


# Integers.
numTree = to_binary_tree([1, 2, 3, 4, 5, 6, 7])
print(numTree)
numBFS = [1, 2, 3, 4, 5, 6, 7]
numDFS = [1, 2, 4, 5, 3, 6, 7]
numIIT = [4, 2, 5, 1, 6, 3, 7]
numPostOrderT = [4, 5, 2, 6, 7, 3, 1]
numPreOrderT = [1, 2, 4, 5, 3, 6, 7]

# Alphabetical.
alphaTree = to_binary_tree(["A", "B", "C", "D", None, "E", "F", None, None, None, None, "G", "H", "I", None])
alphaBFS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
alphaDFS = ["A", "B", "D", "C", "E", "G", "H", "F", "I"]
alphaIIT = ["D", "B", "A", "G", "E", "H", "C", "I", "F"]
alphaPostOrderT = ["D", "B", "G", "H", "E", "I", "F", "C", "A"]
alphaPreOrderT = ["A", "B", "D", "C", "E", "G", "H", "F", "I"]

# Empty.
emptyTree = to_binary_tree([])
