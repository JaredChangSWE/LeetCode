#include <cstddef>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* dfs_inorder(TreeNode* root, int target) {
    if (root == nullptr) return nullptr;
    TreeNode* left = dfs_inorder(root->left, target);
    if (left != nullptr) return left;
    if (root->val == target) return root;
    return dfs_inorder(root->right, target);
}

TreeNode* dfs_preorder(TreeNode* root, int target) {
    if (root == nullptr) return nullptr;
    if (root->val == target) return root;
    TreeNode* left = dfs_preorder(root->left, target);
    if (left != nullptr) return left;
    return dfs_preorder(root->right, target);
}

TreeNode* dfs_postorder(TreeNode* root, int target) {
    if (root == nullptr) return nullptr;
    TreeNode* left = dfs_postorder(root->left, target);
    if (left != nullptr) return left;
    TreeNode* right = dfs_postorder(root->right, target);
    if (right != nullptr) return right;
    return root;
}
