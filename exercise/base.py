# 23-5-21 用于转换32和64进制 自己编的


class Base:
    def __init__(self):
        self.dict_32 = {0: 'a',
                   1: 'b',
                   2: 'c',
                   3: 'd',
                   4: 'e',
                   5: 'f',
                   6: 'g',
                   7: 'h',
                   8: 'i',
                   9: 'j',
                   10: 'k',
                   11: 'l',
                   12: 'm',
                   13: 'n',
                   14: 'o',
                   15: 'p',
                   16: 'q',
                   17: 'r',
                   18: 's',
                   19: 't',
                   20: 'u',
                   21: 'v',
                   22: 'w',
                   23: 'x',
                   24: 'y',
                   25: 'z',
                   26: 'A',
                   27: 'B',
                   28: 'C',
                   29: 'D',
                   30: 'E',
                   31: 'F'}
        self.dict_64 = {0: 'a',
                 1: 'b',
                 2: 'c',
                 3: 'd',
                 4: 'e',
                 5: 'f',
                 6: 'g',
                 7: 'h',
                 8: 'i',
                 9: 'j',
                 10: 'k',
                 11: 'l',
                 12: 'm',
                 13: 'n',
                 14: 'o',
                 15: 'p',
                 16: 'q',
                 17: 'r',
                 18: 's',
                 19: 't',
                 20: 'u',
                 21: 'v',
                 22: 'w',
                 23: 'x',
                 24: 'y',
                 25: 'z',
                 26: 'A',
                 27: 'B',
                 28: 'C',
                 29: 'D',
                 30: 'E',
                 31: 'F',
                 32: 'G',
                 33: 'H',
                 34: 'I',
                 35: 'J',
                 36: 'K',
                 37: 'L',
                 38: 'M',
                 39: 'N',
                 40: 'O',
                 41: 'P',
                 42: 'Q',
                 43: 'R',
                 44: 'S',
                 45: 'T',
                 46: 'U',
                 47: 'V',
                 48: 'W',
                 49: 'X',
                 50: 'Y',
                 51: 'Z',
                 52: '!',
                 53: '@',
                 54: '#',
                 55: '%',
                 56: '^',
                 57: '&',
                 58: '*',
                 59: ',',
                 60: '.',
                 61: '=',
                 62: '-',
                 63: '+'}

    def base32(self, num: int) -> str:
        """32进制转换 倾向于使用小写字母 并且不用数字"""
        s = ''
        if num == 0:
            return 'a'
        elif num < 0:
            num = abs(num)
            s += '-'
        while num:
            temp = num % 32
            s += self.dict_32[temp]
            num //= 32
        return s

    def reBase32(self, s: str) -> int:
        i = 0
        s = s[::-1]
        for _ in range(len(s)):
            for key in self.dict_32:
                if self.dict_32[key] == s[_]:
                    i += key * pow(32, _)
                    break
        return i

    def base64(self, n: int) -> str:
        s = ''
        if n == 0:
            return 'a'
        while n:
            temp = n % 32
            s = self.dict_64[temp] + s
            n //= 64
        return s

    def reBase64(self, s: str) -> int:
        """逆转换至十进制"""
        i = 0
        s = s[::-1]
        for _ in range(len(s)):
            for key in self.dict_64:
                if self.dict_64[key] == s[_]:
                    i += key * pow(64, _)
                    break
        return i


if __name__ == '__main__':
    Base = Base()
    print(Base.base32(4563435))
    print(Base.reBase64('xzqng'))