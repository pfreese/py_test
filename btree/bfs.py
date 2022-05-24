import btrees

def bfs(t: btrees.TreeNode) -> [int]:
    visited = []
    queue = []
    bfsResult = []

    if t is None:
        return bfsResult

    visited = [t]
    queue = [t]
    while queue:
        node = queue[0]
        queue = queue[1:]

        bfsResult.append(node.val)

        if node.left:
            visited.append(node.left)
            queue.append(node.left)
        if node.right:
            visited.append(node.right)
            queue.append(node.right)

    return bfsResult

print(bfs(btrees.simpTree))
print(bfs(btrees.complexTree))
