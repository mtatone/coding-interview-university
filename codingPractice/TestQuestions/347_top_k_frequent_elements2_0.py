from collections import OrderedDict
class Solution:
    @staticmethod
    def topKFrequent(nums, k):
        '''
          - given a list of numbers return the top k most frequent elements
            - create an array of length nums
            - convert it to a set to get unique values
            - iterate through the set of numbers and get the frequency of each number
            - add the number to the index corresponding to the frequency if a number exists just append the number
            - iterate through the array to get the k most frequent elements starting at the end
            - return k most frequent elements
        '''
        # count_store = [[] for i in range(len(nums) + 1)]
        # numset = set(nums)
        # for num in numset:
        #     count_store[nums.count(num)].append(num)
        # ans = []
        # for i in range(len(count_store) - 1, 0, -1):
        #     for a in count_store[i]:
        #         ans.append(a)
        #         if len(ans) == k:
        #             return ans

        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for n, c in count.items():
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for a in freq[i]:
                ans.append(a)
                if len(ans) == k:
                    return ans



# nums = [6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0]
# k = 6
# nums =[4,1,-1,2,-1,2,3]
# k =2
nums = [1,1,1,2,2,3]
k = 2


ans = Solution.topKFrequent(nums=nums, k=k)
print(ans)
