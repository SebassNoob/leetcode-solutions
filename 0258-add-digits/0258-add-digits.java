import java.util.*;
class Solution {
    public int addDigits(int num) {
        while (String.valueOf(num).length() != 1){
            String[] res = String.valueOf(num).toString().split("");
            int temp=0;
            for (String i: res){
                temp += Integer.parseInt(i);
            
            }
            num = temp;
        }
        return num;
        
    }
}