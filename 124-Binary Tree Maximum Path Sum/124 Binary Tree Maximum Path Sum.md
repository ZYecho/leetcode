## 124.Binary Tree Maximum Path Sum

#### Author 康锴

#### [题目链接](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

这道题是要求出二叉树中路径的最大和，这里的路径可以是从二叉树的任意结点出发，终止到任意结点，经不经过根结点都可以。

看到有关树的问题，最先想到的就是最常使用的**深搜**。在对子树深搜之后，我们可以轻易得到包含子结点的最大路径和。对于父结点来说，如果子结点提供的路径和小于0，则肯定会被抛弃；否则就与父结点组成一条路径，返回到上一层供上层结点计算使用。

上述情况考虑的是根结点在最大路径和里的情况，如果最大路径和出现在某一子树中，在代码中只需要做一些小改动即可。在对左右子树分别进行深搜之后，得到的是包含左子结点的最大路径和以及包含右子结点的最大路径和，那么只需要将两者相加再加上当前结点的值，然后与全局的result值进行比较即可。

##### AC代码：

```java
class Solution {
    int result = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        dfs(root);
        return result;
    }
    
    public int dfs(TreeNode node) {
        
        if(node == null)
            return 0;
        
        int left = dfs(node.left);
        int right = dfs(node.right);
        int max = left > right ? left : right;
        result = Math.max(max + node.val, result);
        result = Math.max(left + right + node.val, result);     
        return (max + node.val) > 0 ? (max + node.val) : 0;
    }
}
```

Discuss里的代码与上述思想类似，基本没改动。

##### discussion代码：

```java
public class Solution {
    int maxValue;
    
    public int maxPathSum(TreeNode root) {
        maxValue = Integer.MIN_VALUE;
        maxPathDown(root);
        return maxValue;
    }
    
    private int maxPathDown(TreeNode node) {
        if (node == null) return 0;
        int left = Math.max(0, maxPathDown(node.left));
        int right = Math.max(0, maxPathDown(node.right));
        maxValue = Math.max(maxValue, left + right + node.val);
        return Math.max(left, right) + node.val;
    }
}
```

### -end-

*PS：哈哈哈哈，捡到了一道easy题*