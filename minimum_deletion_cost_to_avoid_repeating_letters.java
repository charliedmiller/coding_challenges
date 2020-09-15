// Charlie Miller
// Leetcode - 1578. Minimum Deletion Cost to Avoid Repeating Letters
// https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/


// Run thru the string once. Keep track of the previous char encountered
// If previous was same, take note with repeats, and calculate max encountered
// cost, and total cost of whole run with repeats
// when a different char encountered, add the total cost - max cost to overall
// cost, and reset all trackers.

class Solution {
    public int minCost(String s, int[] cost) {
        
        //Edge case, there's no string, return 0
        if (s.length() == 0){
            return 0;
        }
        
        
        int total_cost = 0;
        
        //initialize with first character, then loop on the rest
        char prev_char = s.charAt(0);
        int repeats = 1;
        int max_cost = cost[0]; //max cost of repeated run
        int total_char_cost = cost[0]; //total cost of repeated run
        
        
        for (int i = 1;i<s.length();i++){
            char cur_char = s.charAt(i);
            
            //repeat encountered, add to total_char_cost, and calc max cost of run
            if (cur_char == prev_char){
                repeats += 1;
                max_cost = Math.max(max_cost,cost[i]);
                total_char_cost += cost[i];
            }else{
                //New char! 
                
                //Add cost of previous run (only if there were repeats)
                //We get rid of all but one, the one with max cost
                if (repeats > 1){
                    total_cost += total_char_cost - max_cost;
                }
                
                //reset trackers
                repeats = 1;
                max_cost = cost[i];
                total_char_cost = cost[i];
            }
            //prepare for next iteration
            prev_char = cur_char;
        }
        
        //The loop finished, but we need to calculate the cost of 
        //the last run if it was of length more than 1
        if (repeats > 1){
            total_cost += total_char_cost - max_cost;
        }
        
        return total_cost;
    }
}