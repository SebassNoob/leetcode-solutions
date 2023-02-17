class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in [(n+1) for n in range(n)]:
            result = ""
            if i%3 ==0 : result += "Fizz"
            if i%5==0 : result += "Buzz"
            if result =="": result = str(i)
            answer.append(result)
        return answer
