import btrees

def dfs(t: btrees.TreeNode) -> [int]:

    dfsResult = []

    if t is None:
        return dfsResult

    visited = []
    stack = [t]
    while stack:

        node = stack.pop()

        if node not in visited:
            dfsResult.append(node.val)
        visited.append(node)

        # Note: it's important that RIGHT is added to the stack
        # before LEFT, so that LEFT is on the top of the stack and
        # we continue traversing down the left side as much as possible.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return dfsResult


print(dfs(btrees.simpTree))
print(dfs(btrees.complexTree))
