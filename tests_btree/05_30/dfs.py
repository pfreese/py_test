import btrees

def dfs(t: btrees.TreeNode) -> []:

    if t is None:
        return []

    stack = [t]
    visited = []

    while stack:

        node = stack.pop()
        visited.append(node)

        if node.right and node.right not in stack:
            stack.append(node.right)
        if node.left and node.left not in stack:
            stack.append(node.left)

    return [node.val for node in visited]


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
print(numResult)
print(dfs_recursive(btrees.numTree))

alphaResult = dfs(btrees.alphaTree)
assert alphaResult == btrees.alphaDFS
print(alphaResult)
print(dfs_recursive(btrees.alphaTree))

assert dfs(btrees.emptyTree) == []
assert dfs_recursive(btrees.emptyTree) == []
