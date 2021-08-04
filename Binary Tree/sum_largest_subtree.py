class newNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def find_sum(root, ans):
    if not root:
        return 0
    cursum = root.key + find_sum(root.left, ans) + find_sum(root.right, ans)

    ans = max(ans, cursum)
    return ans

root = newNode(1)
root.left = newNode(-2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(-6)
root.right.right = newNode(2)
print(find_sum(root, float("-inf")))
