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


n1 = btrees.TreeNode(val = 5)

simpTree = btrees.to_binary_tree([1, 2, 3, None, None, 4, 5])
complexTree = btrees.to_binary_tree([3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14])

print(bfs(simpTree))
print(bfs(complexTree))
