def dfs_inorder(root, target):
    if root is None:
        return None
    left = dfs_inorder(root.left, target)
    if left is not None:
        return left
    if root.val == target:
        return root
    return dfs_inorder(root.right, target)


def dfs_preorder(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = dfs_preorder(root.left, target)
    if left is not None:
        return left
    return dfs_preorder(root.right, target)


def dfs_postorder(root, target):
    if root is None:
        return None
    left = dfs_postorder(root.left, target)
    if left is not None:
        return left
    right = dfs_postorder(root.right, target)
    if right is not None:
        return right
    return root
