import btrees

def inOrderTraversal(t: btrees.TreeNode) -> []:
    if t is None:
        return []
    return inOrderTraversal(t.left) + [t.val] + inOrderTraversal(t.right)


def preOrderTraversal(t: btrees.TreeNode) -> []:
    if t is None:
        return []
    return [t.val] + preOrderTraversal(t.left) + preOrderTraversal(t.right)



def postOrderTraversal(t: btrees.TreeNode) -> []:
    if t is None:
        return []
    return postOrderTraversal(t.left) + postOrderTraversal(t.right) + [t.val]



print("inOrderTraversal()s:")

numResult = inOrderTraversal(btrees.numTree)
assert numResult == btrees.numIIT
print(numResult)

alphaResult = inOrderTraversal(btrees.alphaTree)
assert alphaResult == btrees.alphaIIT
print(alphaResult)

assert inOrderTraversal(btrees.emptyTree) == []


print("preOrderTraversal()s:")

numResult = preOrderTraversal(btrees.numTree)
assert numResult == btrees.numPreOrderT
print(numResult)

alphaResult = preOrderTraversal(btrees.alphaTree)
assert alphaResult == btrees.alphaPreOrderT
print(alphaResult)

assert preOrderTraversal(btrees.emptyTree) == []


print("postOrderTraversal()s:")

numResult = postOrderTraversal(btrees.numTree)
assert numResult == btrees.numPostOrderT
print(numResult)

alphaResult = postOrderTraversal(btrees.alphaTree)
assert alphaResult == btrees.alphaPostOrderT
print(alphaResult)

assert postOrderTraversal(btrees.emptyTree) == []
