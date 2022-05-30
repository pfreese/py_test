import btrees

# Note: with a binary search tree, it's not actually necessary to keep
# track of the nodes visited.
# But for a more general graph it is.

def bfs(t: btrees.TreeNode) -> []:

    visited = []
    queue = []
    bfsResult = []

    if t is None:
        return bfsResult

    visited = [t]
    queue = [t]
    while queue:

        node = queue[0]
        queue = queue[1:]

        bfsResult.append(node.val)

        if node.left and node.left not in visited:
            visited.append(node.left)
            queue.append(node.left)
        if node.right and node.right not in visited:
            visited.append(node.right)
            queue.append(node.right)

    return bfsResult

numResult = bfs(btrees.numTree)
assert numResult == btrees.numBFS
print(numResult)

alphaResult = bfs(btrees.alphaTree)
assert alphaResult == btrees.alphaBFS
print(alphaResult)

assert bfs(btrees.emptyTree) == []
