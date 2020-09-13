// Charlie Miller
// Leetcode - 216. Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/


// Recursively choose numbers to use for the combination
// keep track of how many moves left, and remaining sum so we don't 
// waste time on impossible paths
// Sequence should only be advancing so if 3 is chosen only numbers afterwards
// will be eligible


class Solution {
//  recursive routine to choose numbers
    private List<List<Integer>> combinationSumk(int k, int n, int start){
//      what we will return
        List<List<Integer>> combos = new ArrayList<>();
        
//      If we have no more turns, or we can't add anymore, we return nothing
        if (n < 0 || k == 0){
            return combos;
        }
//      If there's 1 more number to choose, and that number isn't 
//      eligible, we return nothing
        if (k == 1){
            if (n > 9 || start > n){
                return combos;
            }
        } 
        
//      we'll only iteratate eligble numbers, nothing that overshoots the sum
        int end = Math.min(9,n)+1;
        for(int i=start;i<end;i++){
            
//          Use i as the next number for the sum
            int new_target = n - i;
            
//          If there's 1 more number to use, and we hit that number, return an array of that number!
            if (new_target == 0){
                if (k == 1){
                    combos.add(new ArrayList<Integer>(Arrays.asList(i)));
                }
                break;
            }
            
//          get the list of combinations possible with the new target
            List<List<Integer>> cur_combos = this.combinationSumk(k-1,new_target,i+1);

//          from those combinations, add i to each to get our result            
            for(List<Integer> combo_list:cur_combos){
                combo_list.add(i);
                combos.add(combo_list);
            }
        }
        
        return combos;
    }
    public List<List<Integer>> combinationSum3(int k, int n) {
//      we can't make a combination of each digit that sums to more than 45
        if(n > 45){
            return new ArrayList<>();
        }
        
        return this.combinationSumk(k,n,1);
        
        
        
    }
}