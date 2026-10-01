class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rev = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in rev:
                rev[key] = []
            rev[key].append(word)
        return list(rev.values())
        
        