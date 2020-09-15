// Charlie Miller
// Leetcode - 1583. Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/


// Don't have much time. will explain in later commit

class Solution {
    private int find(int[] arr,int target){
        for(int i = 0;i<arr.length;i++){
            if (arr[i] == target){
                return i;
            }
        }
        return -1;
    }
    
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[] unhappys = new int[n];
        int[] pairings = new int[n];
        
        for (int[]pair:pairs){
            int first = pair[0];
            int second = pair[1];
            pairings[first] = second;
            pairings[second] = first;
        }
        
        
        
        for (int i =0;i<n;i++){
            
            int partner = pairings[i];
            int rank = this.find(preferences[i],partner);
            for (int j = rank-1;j>=0;j--){
                int preferred = preferences[i][j];
                int preferreds_partner_rank = this.find(preferences[preferred],pairings[preferred]);
                int preferreds_curFriend_rank = this.find(preferences[preferred],i);
                
                if (preferreds_curFriend_rank < preferreds_partner_rank){
                    unhappys[i] = 1;
                    unhappys[preferred] = 1;
                }
                    
            }
        }
        int total_unhappys = 0;
        
        for (int i = 0;i<n;i++){
            total_unhappys += unhappys[i];
        }
        
        return total_unhappys;
    }
}