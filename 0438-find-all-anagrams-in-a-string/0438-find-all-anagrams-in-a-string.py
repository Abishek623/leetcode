class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        p = "".join(sorted(list(p)))
        window = ""
        start = 0
        res = []

        for char in s:
            window+=char
            if len(window)==len(p):
                if p == "".join(sorted(list(window))):
                    res.append(start)
                window = window[1:]
                start+=1
        return res