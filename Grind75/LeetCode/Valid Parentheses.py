class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
        return not stack


if __name__ == "__main__":
    # Instantiate the class
    solution = Solution()
    # Call the method with test parameters
    result = solution.isValid("([{}])")
    print(result)
    
    # Pause the program
    input("Press Enter to close...")
