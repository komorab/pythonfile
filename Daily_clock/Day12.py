# 2022-2-20 717 1比特与2比特字符
# 给定数组bits，如果最后一个只能是一比特字符则返回True
# 1bit为0，2bit由01或11构成


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i, n = 0, len(bits)
        while i < n - 1:
            i += bits[i] + 1
        return i == n - 1
