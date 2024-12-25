" Very easy but I want to keep github stereak alive not repeat something  I already did "

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        num = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                num += 1
            elif s[i] == " " and num == 0:
                continue
            else:
                break
        return num