# 2022-3-1 6 Z字形变换
# 耗时长 内存占用大 不过确实能用
"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        ans = ''
        if n <= numRows or numRows == 1:
            return s
        else:
            for i in range(numRows):
                if i == 0 or i == numRows-1:
                    position = [_ for _ in range(i, n, 2*numRows-2)]
                    for pos in position:
                        ans += s[pos]
                else:
                    position = [_ for _ in range(i, n, 2*numRows-2)] + [j for j in range(2*numRows-2-i, n, 2*numRows-2)]
                    position.sort()
                    for pos in position:
                        ans += s[pos]
            return ans
