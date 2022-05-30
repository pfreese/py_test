import btrees

def dfs(t: btrees.TreeNode) -> []:

    # Note: keep track of the nodes here, and then return the values at
    # the end if desired. This allows for the values to not be unique.
    visitedNodes = []

    if t is None:
        return visitedNodes

    stack = [t]
    while stack:

        node = stack.pop()

        if node not in visitedNodes:
            visitedNodes.append(node)

        # Note: it's important that RIGHT is added to the stack
        # before LEFT, so that LEFT is on the top of the stack and
        # we continue traversing down the left side as much as possible.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return [node.val for node in visitedNodes]


numResult = dfs(btrees.numTree)
assert numResult == btrees.numDFS
print(numResult)

alphaResult = dfs(btrees.alphaTree)
assert alphaResult == btrees.alphaDFS
print(alphaResult)

assert dfs(btrees.emptyTree) == []
