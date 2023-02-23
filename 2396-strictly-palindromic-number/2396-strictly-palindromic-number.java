import java.util.*;
class Solution {
    public List<String> convertBase(int n){
        List<String> res = new ArrayList<>();
        for (int i =2; i<=n-2; i++){
            String a = Integer.toString(Integer.parseInt(Integer.valueOf(n).toString(), 10),i);
            res.add(a);
            
        }
        return res;
    }
    
    public boolean isStrictlyPalindromic(int n) {
        // generate n expressed in 2 to n-2 base
        List<String> bases = convertBase(n);
        
        for (String j : bases){
            StringBuilder k = new StringBuilder(j);
            
            
            if (!(k.reverse().toString().equals(j))){
               return false; 
            }
            
        }
        return true;
        
        
        
    }
}