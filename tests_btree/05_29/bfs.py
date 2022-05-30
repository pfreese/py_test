import btrees

# Note: with a binary search tree, it's not actually necessary to keep
# track of the nodes visited.
# But for a more general graph it is.

def bfs(t: btrees.TreeNode) -> []:
    if t is None:
        return []

    nodesVisited = []
    queue = [t]

    while queue:
        node = queue[0]
        queue = queue[1:]

        assert node not in nodesVisited
        nodesVisited.append(node)

        if node.left and node.left not in nodesVisited:
            queue.append(node.left)
        if node.right and node.right not in nodesVisited:
            queue.append(node.right)
    return [node.val for node in nodesVisited]


numResult = bfs(btrees.numTree)
assert numResult == btrees.numBFS
print(numResult)

alphaResult = bfs(btrees.alphaTree)
assert alphaResult == btrees.alphaBFS
print(alphaResult)

assert bfs(btrees.emptyTree) == []
