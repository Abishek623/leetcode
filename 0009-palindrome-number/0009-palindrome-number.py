class Solution(object):
    def isPalindrome(self, x):
        original =x
        reversed=0
        while x>0:
            u=x%10
            reversed=reversed*10+u
            x=x//10
        if original==reversed:
            return True
        else:
            return False


        