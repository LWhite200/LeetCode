" Pretty simple check to see if we are currently have a valid run "
" Store indexes of open and pop on the closed - check when pop to see if the curr amount is biggest "

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        stack.append(-1)
        max_len = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i) # append the index
            else:

                stack.pop() # If no opening, we pop to see if what is present is valid

                if not stack:
                    stack.append(i) # since the stack is empty, we cannot go further
                else:
                    max_len = max(max_len, i - stack[-1]) # check if the current length is bigger than the current max

        return max_len