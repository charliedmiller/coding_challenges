// Charlie Miller
// Leetcode - Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

import java.lang.Math;

/*
Split array by locations of 0s
Find Max Product subarray of splits, then take the max of the splits
Max Product subarray (no zeros) is the whole thing unless it has odd number of negatives
When there's odd negatives, it's one of 2:
Everything up to the last negative
Everything after the first negative
*/

class Solution {
//multiply the given array from start to end. Return MIN_VALUE if empty
    private int pi(int[] arr,int start,int end){
        int result = 1;
        Boolean empty = true;
        
        for(int i=start;i<end;i++){
            result *= arr[i];
            empty = false;
        }

        return empty ? Integer.MIN_VALUE : result;
    }
    
    // find the max subarray product, knowing there are no 0s
    private int maxProductNoZero(int[] subarr){
        
        //Find out how many negatives there are, and the locations of the 
        //first and last negatives in the array
        int negatives = 0;
        int first_negative = -1;
        int last_negative = subarr.length;
        
        for(int i = 0;i<subarr.length;i++){
            if(subarr[i]<0){
                if(negatives == 0){
                    first_negative = i;
                }
                negatives += 1;
                last_negative = i;
            }
        }
        
        //If there's an even amt of negatives, the max product uses the whole array
        if(negatives % 2 == 0){
            return this.pi(subarr,0,subarr.length);
        }
        
        //otherwise it uses the array until the last negative, or from the first
        //negative to the end
        int largest = Integer.MIN_VALUE;
        int[] candidates = {
                             this.pi(subarr,0,last_negative),
                             this.pi(subarr,first_negative+1,subarr.length)
                             };
        for(int cand:candidates){
            largest = Math.max(largest,cand);
        }
        
        return largest;
        
    }
    
    //All magnitude is lost when multiplied by 0
    //Divide and conquer all subarrays split by 0's
    public int maxProduct(int[] nums) {
        
        //At the very least, the max subarray will be the max value seen
        //in the subarray
        int cur_max = Integer.MIN_VALUE;
        for(int num : nums){
            cur_max = Math.max(cur_max,num);
        }
        
        //Split arrays by 0's determine their largest product, then
        // consider it for the overall max product
        int beg = 0;
        int end = 0;
        for(end=0;end<nums.length;end++){
            if(nums[end] == 0){
                //Could probably just send start & end of subarray instead of copying a new one
                int[] subarr = Arrays.copyOfRange(nums,beg,end);
                int cand_max = this.maxProductNoZero(subarr);
                cur_max = Math.max(cur_max,cand_max);
                beg = end+1;
            }
        }
        //remainder of array should also be considered        
        int[] subarr = Arrays.copyOfRange(nums,beg,end);
        int cand_max = this.maxProductNoZero(subarr);
        cur_max = Math.max(cur_max,cand_max);
            
        return cur_max;
    }
    
}