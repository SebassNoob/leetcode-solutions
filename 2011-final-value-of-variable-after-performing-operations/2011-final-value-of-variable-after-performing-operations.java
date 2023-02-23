class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for (String op : operations){
            // an operator can always be found at pos 1
            if(op.charAt(1) == '+'){
                x++;
            }
            else if(op.charAt(1) == '-'){
                x--;
            }
        }
        return x;
    }
}