class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] res = new int[2*n];
        int p1 = 0; 
        int p2 = n;
        int ind = 0;
        while (p2< 2*n){
            res[ind] = nums[p1];
            res[ind+1] = nums[p2];
            p1++;
            p2++;
            ind+=2;
            
        }
        
        return res;
    }
}