import btrees

def inOrderTraversal(t: btrees.TreeNode) -> [int]:
    result = []
    if t is None:
        return result
    result += inOrderTraversal(t.left)
    result.append(t.val)
    result += inOrderTraversal(t.right)

    return result

def preOrderTraversal(t: btrees.TreeNode) -> [int]:
    result = []
    if t is None:
        return result
    result.append(t.val)
    result += preOrderTraversal(t.left)
    result += preOrderTraversal(t.right)

    return result

def postOrderTraversal(t: btrees.TreeNode) -> [int]:
    result = []
    if t is None:
        return result
    result += postOrderTraversal(t.left)
    result += postOrderTraversal(t.right)
    result.append(t.val)

    return result

print("inOrderTraversal()s:")
print(inOrderTraversal(btrees.simpTree))
print(inOrderTraversal(btrees.complexTree))

print("preOrderTraversal()s:")
print(preOrderTraversal(btrees.simpTree))
print(preOrderTraversal(btrees.complexTree))

print("postOrderTraversal()s:")
print(postOrderTraversal(btrees.simpTree))
print(postOrderTraversal(btrees.complexTree))
