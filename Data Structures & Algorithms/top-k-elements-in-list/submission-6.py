class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #After learning about buckets
        count = Counter(nums)

        buckets =[]

        # plus 1 so that the frequency bucket correlates to the index since possible frequencies is len(nums) because if len is 3 and they are all 3s then there needs to be 4 buckets so that the frequency bucket 3 can have 3 in it at index 3
        for i in range(len(nums)+1):
            buckets.append([])

        for num, freq in count.items():
            buckets[freq].append(num)
        

        result=[]
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result

        return []

        
        # FIRST ATTEMPT
        # storage = {}
        # finalList=[]

        # for num in nums:
        #     if(storage.get(num) is None):
        #         storage[num] = 1
        #     else:
        #         storage[num] += 1

        # vals = sorted(storage.items(), key=lambda x: x[1], reverse=True)[:k]
        # for item in vals:
        #     finalList.append(item[0])

        # return finalList