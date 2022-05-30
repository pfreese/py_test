import btrees

def inOrderTraversal(t: btrees.TreeNode) -> [int]:


def preOrderTraversal(t: btrees.TreeNode) -> [int]:


def postOrderTraversal(t: btrees.TreeNode) -> [int]:


print("inOrderTraversal()s:")
print(inOrderTraversal(btrees.simpTree))
print(inOrderTraversal(btrees.complexTree))

print("preOrderTraversal()s:")
print(preOrderTraversal(btrees.simpTree))
print(preOrderTraversal(btrees.complexTree))

print("postOrderTraversal()s:")
print(postOrderTraversal(btrees.simpTree))
print(postOrderTraversal(btrees.complexTree))
