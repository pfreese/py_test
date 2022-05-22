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
            print("Adding!")
            dfsResult.append(node.val)
        visited.append(node)

        # Note: it's important that RIGHT is added to the stack
        # before LEFT, so that LEFT is on the top of the stack and
        # we continue traversing down the left side as much as possible.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print(f"Stack length is: {len(stack)}")

    return dfsResult


simpTree = btrees.to_binary_tree([1, 2, 3, None, None, 4, 5])
complexTree = btrees.to_binary_tree([3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14])

print(dfs(simpTree))
print(dfs(complexTree))
