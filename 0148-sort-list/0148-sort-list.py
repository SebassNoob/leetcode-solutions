# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def merge_sort(self, array):
        if len(array) <= 1:
            return array
        lst1, lst2 = array[0: math.floor(len(array)/2)], array[math.floor(len(array)/2) : len(array)]
        lst1 = self.merge_sort(lst1)
        lst2 = self.merge_sort(lst2)
        return self.merge(lst1, lst2)
    
    def merge(self, lst1, lst2):
        i, j = 0, 0
        res = []
        while i < len(lst1) and j < len(lst2) :
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1
        while i < len(lst1):
            res.append(lst1[i])
            i+= 1
        while j < len(lst2):
            res.append(lst2[j])
            j+=1
        return res
        
        
        
        
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get all the values in the list
        if not head: return None
        cur = head
        result = []
        while cur.next is not None:
            result.append(cur.val)
            cur = cur.next
        result.append(cur.val)
        
        a = [ListNode(val=i) for i in self.merge_sort(result)]
        for i, node in enumerate(a):
            if i+1 < len(a):
                node.next = a[i+1]
        return a[0]
        
        
        
        
        