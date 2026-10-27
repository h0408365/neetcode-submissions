class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map=defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            anagram_map[sorted_string].append(string)
        return list(anagram_map.values())
