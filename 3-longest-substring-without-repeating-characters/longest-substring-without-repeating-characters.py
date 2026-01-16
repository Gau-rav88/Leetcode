class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        hmap = {}
        max_len = start = 0

        for i in range(len(s)):
            if s[i] in hmap and start <= hmap[s[i]]:
                start = hmap[s[i]] + 1
            else:
                max_len = max(max_len,i - start + 1)
            hmap[s[i]] = i
        return(max_len)