import btrees

# Note: with a binary search tree, it's not actually necessary to keep
# track of the nodes visited.
# But for a more general graph it is.

def bfs(t: btrees.TreeNode) -> []:
    # Want to use a queue.
    if t is None:
        return []

    queue = [t]
    visited = [t]
    result = []
    while queue:
        node = queue[0]
        queue = queue[1:]
        result.append(node)

        if node.left and node.left not in visited:
            visited.append(node.left)
            queue.append(node.left)
        if node.right and node.right not in visited:
            visited.append(node.right)
            queue.append(node.right)
    return [node.val for node in result]



numResult = bfs(btrees.numTree)
assert numResult == btrees.numBFS
print(numResult)

alphaResult = bfs(btrees.alphaTree)
assert alphaResult == btrees.alphaBFS
print(alphaResult)

assert bfs(btrees.emptyTree) == []
