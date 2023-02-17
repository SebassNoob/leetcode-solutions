# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        res = []
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        
        if [n for n in reversed(res)] == res:

            return True
        return False