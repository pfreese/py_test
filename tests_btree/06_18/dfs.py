import btrees

def dfs(t: btrees.TreeNode) -> []:
    if t is None:
        return []
    stack = [t]
    visited = [t]
    result = []
    while stack:
        node = stack.pop()
        result.append(node)

        # Check right first.
        if node.right and node.right not in visited:
            stack.append(node.right)
            visited.append(node.right)
        if node.left and node.left not in visited:
            stack.append(node.left)
            visited.append(node.left)
    return [node.val for node in result]


def dfs_recursive(t: btrees.TreeNode) -> []:
    def dfs_recursive_helper(t, visited):
        if t is None or t in visited:
            return []
        visited.append(t)
        return [t.val] + dfs_recursive_helper(t.left, visited) + dfs_recursive_helper(t.right, visited)
    return dfs_recursive_helper(t, [])


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
