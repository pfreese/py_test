import btrees

def dfs(t: btrees.TreeNode) -> []:

    if t is None:
        return []

    result = []

    stack = [t]
    visited = [t]

    while stack:
        if t.right and t.right not in visited:
            visited.append(t.right)
            stack.append(t.right)

        if t.left and t.left not in visited:
            visited.append(t.left)
            stack.append(t.left)






numResult = dfs(btrees.numTree)
assert numResult == btrees.numDFS
print(numResult)

alphaResult = dfs(btrees.alphaTree)
assert alphaResult == btrees.alphaDFS
print(alphaResult)

assert dfs(btrees.emptyTree) == []
