/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.*;
class Solution {
    public ArrayList<Integer> traverse(TreeNode a, ArrayList<Integer> lst){
        if (a != null){
            this.traverse(a.left, lst);
            lst.add(a.val);
            this.traverse(a.right, lst);
        }
        return lst;
    }

    public Integer smallestDiff(ArrayList<Integer> lst){
        Integer prev = lst.get(0);
        ArrayList<Integer> res = new ArrayList<>();
        for (Integer i = 1; i< lst.size(); i++){
            Integer temp = lst.get(i) - prev;
            prev = lst.get(i);
            res.add(temp);
        }
        Collections.sort(res);
        return res.get(0);
    }
    
    public int minDiffInBST(TreeNode root) {
        
        ArrayList<Integer> lst = new ArrayList<>();
        lst = traverse(root, lst);
        Integer diffn = smallestDiff(lst);

        return (int) diffn;
    }
}