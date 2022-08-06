from collections import OrderedDict
class Solution:
    @staticmethod
    def topKFrequent(nums, k):
        '''
          - given a list of numbers return the top k most frequest elements
            - convert it to a set to get unique values
            - create an array of length k
            - iterate through the list of numbers
            - if the frequency count is greater than what is in the array, add it
            - return the array
        '''
        #can improve speed by getting ride of the array and use a list instead
        if len(nums) == 1:
            return nums
        numset = set(nums)
        store = [] # 2D array in which the sub array is [<item>, <frequency>]
        for num in numset:
            freq = nums.count(num)
            store.append([num, freq])
        store.sort(key=lambda x: x[1], reverse=True)
        # store2 = OrderedDict(sorted(store.items(), key=lambda item: item[1], reverse=True))
        flat_list = []
        for i in range(k):
            flat_list.append(store[i][0])
        return flat_list


# nums = [6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0]
# k = 6
# nums =[4,1,-1,2,-1,2,3]
# k =2
nums = [1,1,1,2,2,3]
k = 2


ans = Solution.topKFrequent(nums=nums, k=k)
print(ans)
