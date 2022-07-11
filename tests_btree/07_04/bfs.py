import btrees

from collections import deque

# Note: with a binary search tree, it's not actually necessary to keep
# track of the nodes visited.
# But for a more general graph it is.

def bfs(t: btrees.TreeNode) -> []:
    if t is None:
        return []

    # Need to keep track of visited.
    visited = set()
    visited.add(t)

    result = []

    #
    queue = deque()
    queue.append(t)

    while len(queue) > 0:
        node = queue.popleft()
        result.append(node)

        if node.left and node.left not in visited:
            visited.add(node.left)
            queue.append(node.left)
        if node.right and node.right not in visited:
            visited.add(node.right)
            queue.append(node.right)

    return [node.val for node in result]





numResult = bfs(btrees.numTree)
assert numResult == btrees.numBFS
print(numResult)

alphaResult = bfs(btrees.alphaTree)
assert alphaResult == btrees.alphaBFS
print(alphaResult)

assert bfs(btrees.emptyTree) == []
