import btrees

def inOrderTraversal(t: btrees.TreeNode) -> []:
    result = []
    if t is None:
        return result
    result += inOrderTraversal(t.left)
    result.append(t.val)
    result += inOrderTraversal(t.right)

    return result

def preOrderTraversal(t: btrees.TreeNode) -> []:
    result = []
    if t is None:
        return result
    result.append(t.val)
    result += preOrderTraversal(t.left)
    result += preOrderTraversal(t.right)

    return result

def postOrderTraversal(t: btrees.TreeNode) -> []:
    result = []
    if t is None:
        return result
    result += postOrderTraversal(t.left)
    result += postOrderTraversal(t.right)
    result.append(t.val)

    return result

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
