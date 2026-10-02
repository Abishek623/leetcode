class Solution(object):
    def strStr(self, haystack, needle):
        for i,v in enumerate(haystack):
            if v==needle[0]:
                if needle==haystack[i:i+len(needle)]:
                    return i
                
        return -1
                
