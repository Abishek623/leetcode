# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr = head
        s = []
        while curr:
            s.append(curr.val)
            curr = curr.next
        
        i = 0
        j = len(s) - 1

        while i < j:

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True