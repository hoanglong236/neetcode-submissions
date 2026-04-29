class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for string in strs:
            seq = [0] * 26
            for c in string:
                seq[ord(c) - ord('a')] += 1

            ans.setdefault(tuple(seq), []).append(string)
        return list(ans.values())