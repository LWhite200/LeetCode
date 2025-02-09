class Solution:
    def calculate(self, s: str) -> int:
        cur = res = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in ['+', '-']:
                res += sign * cur
                sign = 1 if c == '+' else -1
                cur = 0
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ")":
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + sign * cur