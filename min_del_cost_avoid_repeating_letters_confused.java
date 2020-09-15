//Charlie Miller

// The following attempts leetcode 1578. Minimum Deletion Cost to Avoid Repeating Letters
// https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
// Though it solves for getting min cost to have no letters repeat in the whole string
// (not in sequences) I felt it was worth keeping

class Solution {
    public int minCost(String s, int[] cost) {
        HashMap<Character,Integer> maxCost = new HashMap<>();
        HashMap<Character,Integer> totalCost = new HashMap<>();
        
        for(int i=0;i<s.length();i++){
            char cur_char = s.charAt(i);
            int next_min;
            int next_cost;
            if (maxCost.containsKey(cur_char)){
                next_min = Math.max(maxCost.get(cur_char),cost[i]);
                next_cost = totalCost.get(cur_char) + cost[i];
            }else{
                next_cost = cost[i];
                next_min = cost[i];
            }
            
            totalCost.put(cur_char,next_cost);
            maxCost.put(cur_char,next_min);
        }
        
        int total_cost = 0;
        
        for(Map.Entry<Character,Integer> entry:totalCost.entrySet()){
            total_cost += entry.getValue() - maxCost.get(entry.getKey());
            System.out.format("Char %c new cost %d\n",entry.getValue(),total_cost);
        }
        
        return total_cost;
    }
}