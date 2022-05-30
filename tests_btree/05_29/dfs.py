import btrees

def dfs(t: btrees.TreeNode) -> []:

    if t is None:
        return []

    # Keep track of the nodes visited.
    nodesVisited = []

    stack = [t]

    while stack:
        node = stack.pop()

        if node not in nodesVisited:
            nodesVisited.append(node)

        if node.right and node.right not in nodesVisited:
            stack.append(node.right)
        if node.left and node.left not in nodesVisited:
            stack.append(node.left)
    return [node.val for node in nodesVisited]



numResult = dfs(btrees.numTree)
assert numResult == btrees.numDFS
print(numResult)

alphaResult = dfs(btrees.alphaTree)
assert alphaResult == btrees.alphaDFS
print(alphaResult)

assert dfs(btrees.emptyTree) == []
