class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        ord_a = ord('a')
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord_a] += 1
            res[tuple(count)].append(s)
        return list(res.values())