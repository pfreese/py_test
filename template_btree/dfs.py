import btrees

def dfs(t: btrees.TreeNode) -> []:


def dfs_recursive(t: btrees.TreeNode) -> []:


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
