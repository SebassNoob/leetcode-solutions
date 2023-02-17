/*



answer = []
        for i in [(n+1) for n in range(n)]:
            result = ""
            if i%3 ==0 : result += "Fizz"
            if i%5==0 : result += "Buzz"
            if result =="": result = str(i)
            answer.append(result)
        return answer


*/
import java.util.*;
class Solution {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> a = new ArrayList<>();
        
        // populate
        for (Integer i = 1; i< n+1; i++){
            StringBuilder s = new StringBuilder();
            boolean isMultiple = false;
            if (i % 3 == 0){s.append("Fizz"); isMultiple = true;}
            if (i % 5 == 0){s.append("Buzz"); isMultiple = true;}
            
            if (isMultiple){a.add(s.toString());}
            
            else{a.add(i.toString());}
            
        }
        return a;
        
    }
}