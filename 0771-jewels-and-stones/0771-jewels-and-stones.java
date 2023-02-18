class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int res = 0;
        for (String stone: stones.split("")){
            if (jewels.contains(stone)){
               res++;
            }
        }
        return res;
    }
}