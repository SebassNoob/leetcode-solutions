class Solution {
    public int maxDepth(String s) {
        int count = 0;
        int max = 0;
        for (char c: s.toCharArray()) {
            if (c == '(') {
                count += 1;
                if (count > max) {
                    max = count;
                }
            }
            if (c == ')') {
                count -= 1;
            }
            
        }
        return max;
        
    }
}