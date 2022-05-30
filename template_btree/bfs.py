import btrees

# Note: with a binary search tree, it's not actually necessary to keep
# track of the nodes visited.
# But for a more general graph it is.

def bfs(t: btrees.TreeNode) -> []:



numResult = bfs(btrees.numTree)
assert numResult == btrees.numBFS
print(numResult)

alphaResult = bfs(btrees.alphaTree)
assert alphaResult == btrees.alphaBFS
print(alphaResult)

assert bfs(btrees.emptyTree) == []
