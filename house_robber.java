// Charlie Miller
// Leetcode - 198. House Robber
// https://leetcode.com/problems/house-robber/


// Recursively choose whether to rob or not rob
// return the max of the two choices
// When we rob, we'll have no choice but to not rob the next
// Record previous answers so we don't have to do them again

class Solution {
    //Record previous answers, in dynamic programming hashmap
    private HashMap<String,Integer> dp = new HashMap<String,Integer>();
    
    //Stringify arguments for each call of robHouses so they can be put into the hashmap
    private String stringify(int start,Boolean robbed_prev){
        return String.format("%d%b",start,robbed_prev);
    }
    
    //main recursive function to calculate max value
    private int robHouses(int[] nums,int start,Boolean robbed_prev){
        
        //If we've seen this problem before, return its recorded answer
        String arg_hashable = this.stringify(start,robbed_prev);
        if (this.dp.containsKey(arg_hashable)){
            return this.dp.get(arg_hashable);
        }
        
        
        int ans = 0;
        //If we're at the end, return the value if we didn't rob the previous
        if (start == nums.length-1){
            ans = robbed_prev ? 0 : nums[start];
            
        //If we robbed the previous, we have no choice but to move on
        }else if (robbed_prev){
            ans = this.robHouses(nums,start+1,false);
        
        //Choose to rob or not rob. Robbing means guarantee not robbing the next
        }else{
            int rob_house = this.robHouses(nums,start+1,true) + nums[start];
            int dont_rob = this.robHouses(nums,start+1,false);
            ans = Math.max(rob_house,dont_rob);
        }
        
        //Record our answer
        this.dp.put(arg_hashable,ans);
        return ans;
    }
    public int rob(int[] nums) {
        //Return 0 when there are no houses
        if (nums.length == 0){
            return 0;
        }
        
        return this.robHouses(nums,0,false);
    }
}