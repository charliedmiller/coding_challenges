// Charlie Miller
// Leetcode - 1022. Sum of Root To Leaf Binary Numbers [Java]
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


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

//I've started to write in Java to get familiar for interviews. At some point
//I should get to almost same level as Python. Given, Java has a higher skill
//ceiling


// Keep track of each path to the leaves. 
// When a leaf is encountered, combine the path to form the binary number
// add the binary number to a list of all leaf numbers encountered
// once the entire tree is traversed, sum all leaf numbers



class Solution {
    // Keep track of the numbers encountered at leaves
    private ArrayList<Integer> numbers = new ArrayList<Integer>();
    
    //Recursively find leaves, keeping track of the path so far
    public void add_numbers(TreeNode root,ArrayList<Integer> path){

        //Parent only had one child, do nothing
        if (root == null)
            return;
            
        // add to our path
        path.add(root.val);
            
        //we are at a leaf. Convert seen path to a number and add it to the list
        if (root.left == null && root.right == null){
            StringBuilder leafnum_str = new StringBuilder();
            
            for (Integer digit:path){
                leafnum_str.append(digit.toString());
            }
            
            int leaf_num = Integer.parseInt(leafnum_str.toString(),2);
            numbers.add(leaf_num);

            // Pop from our list since we're now backtracking
            path.remove(path.size()-1);
            return;
        }
        
        // We're not at the end, keep going
        this.add_numbers(root.left,path);
        this.add_numbers(root.right,path);

        // we're done with this node, pop our path off
        path.remove(path.size()-1);

        return;
        
    }

    //Get the numbers formed by each leaf, then sum them
    public int sumRootToLeaf(TreeNode root) {
        // Get numbers into numbers list
        this.add_numbers(root,new ArrayList<Integer>());

        //Sum the numbers       
        int sum = 0;
        for(int number:this.numbers ){
            sum += number;
        }
            
        return sum;
    }
}