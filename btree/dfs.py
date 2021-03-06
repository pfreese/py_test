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


def dfs_recursive_helper(t: btrees.TreeNode, visited = None) -> []:
    if visited is None:
        visited = []
    if t not in visited:
        visited.append(t)
    if t.left and t.left not in visited:
        dfs_recursive_helper(t.left, visited)
    if t.right and t.right not in visited:
        dfs_recursive_helper(t.right, visited)
    return visited

def dfs_recursive(t: btrees.TreeNode) -> []:
    if t is None:
        return []
    return [node.val for node in dfs_recursive_helper(t)]


numResult = dfs(btrees.numTree)
assert numResult == btrees.numDFS
assert dfs_recursive(btrees.numTree) == btrees.numDFS
print(numResult)

alphaResult = dfs(btrees.alphaTree)
assert alphaResult == btrees.alphaDFS
assert dfs_recursive(btrees.alphaTree) == btrees.alphaDFS
print(alphaResult)

assert dfs(btrees.emptyTree) == []
assert dfs_recursive(btrees.emptyTree) == []
