class Solution:
    def myAtoi(self, s: str) -> int:
        sl = s.strip()
        if not sl:
            return 0

        negative = False
        out = 0
        i = 0

        
        if sl[0] == '-':
            negative = True
            i = 1
        elif sl[0] == '+':
            i = 1
        elif not sl[0].isnumeric():
            return 0

        
        while i < len(sl) and sl[i].isnumeric():
            out = out * 10 + (ord(sl[i]) - ord('0'))

            if not negative and out > 2147483647:
                return 2147483647
            if negative and out > 2147483648:
                return -2147483648

            i += 1

        return -out if negative else out
