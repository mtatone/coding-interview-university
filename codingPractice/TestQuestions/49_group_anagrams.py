from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]
        else:
            '''
                - create a store of all anagrams as you iterate through the list
                - create a hashed representation of all unique chars and the # of occurrences (see below)
                - see if the set exists in the store
                - if it does append it to the array
                - add it to the hash map
            '''

            anagram_store = defaultdict(list)  # unique characters : [array of all anagrams]
            '''
             defaultdict will initialize a dictionary where the values are an empty list. 
             This allows you to just append automatically without having to deal with edge cases
            '''
            for strng in strs:
                strng_key = Solution.generate_key(strng)
                anagram_store[strng_key].append(strng)
            # print(anagram_store)
            return anagram_store.values()

            # creating a hash representative of the anagram of the string
            # format: LETTER#OCCURENCELETTER#OCCURENCE

    @staticmethod
    def generate_key(string):
        s_set = set(sorted(string))
        key = ""
        for letter in s_set:
            key = key + letter + str(string.count(letter))
        return key