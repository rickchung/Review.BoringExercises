"""https://leetcode.com/problems/group-anagrams/
"""
# %%

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Group anagrams together 
        """
        def get_cnt(s):
            cnt = [0] * ord('a')
            for i in s:
                cnt[ord(i) - ord('a')] += 1
            return tuple(cnt)

        rt = {}

        for s in strs:
            key = get_cnt(s)
            sack = rt.get(key, [])
            sack.append(s)
            rt[key] = sack

        return [v for v in rt.values()]


s = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

s.groupAnagrams(strs)
