class Solution(object):
    def groupAnagrams(self, strs):
       hashmap = defaultdict(list)

       for word in strs:
            count=[0]*26
            for letter in word:
                count[ord(letter)-ord('a')] += 1

            hashmap[tuple(count)].append(word)

       return hashmap.values()
        