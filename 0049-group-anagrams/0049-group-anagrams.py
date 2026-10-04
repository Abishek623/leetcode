class Solution(object):
    def groupAnagrams(self, strs):
        anagram={}
        for word in strs:
            aranged=''.join(sorted(word))
            if aranged not in anagram:
                anagram[aranged]=[]
            anagram[aranged].append(word)
        return list(anagram.values())

