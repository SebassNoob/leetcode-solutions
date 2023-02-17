class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = [sum(customer) for customer in accounts]
        return max(total)
        
