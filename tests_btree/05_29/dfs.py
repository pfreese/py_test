import btrees

def dfs(t: btrees.TreeNode) -> []:



numResult = dfs(btrees.numTree)
assert numResult == btrees.numDFS
print(numResult)

alphaResult = dfs(btrees.alphaTree)
assert alphaResult == btrees.alphaDFS
print(alphaResult)

assert dfs(btrees.emptyTree) == []
