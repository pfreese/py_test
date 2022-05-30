import btrees

# Breadth-first search is done with a queue (FIFO).

def bfs(t: btrees.TreeNode) -> [int]:

    if t is None:
        return []

    result = []
    nodesQueue = [t]

    while nodesQueue:
        thisNode = nodesQueue[0]
        nodesQueue = nodesQueue[1:]
        result.append(thisNode.val)

        if thisNode.left:
            nodesQueue.append(thisNode.left)
        if thisNode.right:
            nodesQueue.append(thisNode.right)

    return result





print(bfs(btrees.simpTree))
print(bfs(btrees.complexTree))
