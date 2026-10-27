class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_map = defaultdict(int)
        output = []

        for num in nums:
            int_map[num] += 1
        print("int_map",int_map)
        sorted_values = sorted(int_map.items(), key=lambda x: x[1])
        print("sorted_values",sorted_values)
        
        while len(output) < k:
            output.append(sorted_values.pop()[0])  

        return output






        
       