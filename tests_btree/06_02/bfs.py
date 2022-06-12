import btrees

# Note: with a binary search tree, it's not actually necessary to keep
# track of the nodes visited.
# But for a more general graph it is.

# Want a queue.

def bfs(t: btrees.TreeNode) -> []:

    if t is None:
        return []

    visited = [t]
    result = []
    queue = [t]

    while queue:
        node = queue[0]
        result.append(node)
        queue = queue[1:]

        if node.left and node.left not in visited:
            queue.append(node.left)
            visited.append(node.left)
        if node.right and node.right not in visited:
            queue.append(node.right)
            visited.append(node.right)
    return [node.val for node in result]




numResult = bfs(btrees.numTree)
assert numResult == btrees.numBFS
print(numResult)

alphaResult = bfs(btrees.alphaTree)
assert alphaResult == btrees.alphaBFS
print(alphaResult)

assert bfs(btrees.emptyTree) == []
