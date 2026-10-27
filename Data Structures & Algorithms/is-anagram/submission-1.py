class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        print("sort_s",sort_s)
        print("sort_t",sort_t)
        return sort_t == sort_s