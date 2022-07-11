import btrees

from collections import deque

def dfs(t: btrees.TreeNode) -> []:
    if t is None:
        return []

    stack = deque()
    stack.append(t)

    visited = set()
    visited.add(t)

    result = []

    while len(stack) > 0:

        node = stack.pop()
        result.append(node)

        if node.right and node.right not in visited:
            visited.add(node.right)
            stack.append(node.right)
        if node.left and node.left not in visited:
            visited.add(node.left)
            stack.append(node.left)
    return [node.val for node in result]




def dfs_recursive(t: btrees.TreeNode) -> []:
    if t is None:
        return []
    return [t.val] + dfs_recursive(t.left) + dfs_recursive(t.right)


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
