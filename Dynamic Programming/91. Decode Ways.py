class Solution:

    # for a give string of numbers, we must map them to letters
    # based on their place in the alphabet, however there are double digits
    # so to get the number of messages possible...

    def numDecodings(self, s: str) -> int:
        # dp is a dictionary that will store the number of ways to decode the string starting from each index.
        # Initialize dp with a base case: there's 1 way to decode an empty string (when we're at the end of the input string).
        dp = {len(s): 1}

        # Traverse the string in reverse order, starting from the last character and moving towards the first.
        for i in range(len(s) - 1, -1, -1):
            # If the current character is '0', it can't be decoded on its own, so set dp[i] to 0.
            if s[i] == "0":
                dp[i] = 0
            else:
                # Otherwise, dp[i] is initialized to dp[i + 1], meaning the number of decodings starting at this character
                # is at least as many as the number of decodings starting from the next character.
                dp[i] = dp[i + 1]

            # Check if the current character and the next character form a valid two-digit number that can be decoded.
            # This happens if the current character is '1', or if it's '2' and the next character is between '0' and '6'.
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                # If the above condition is true, add the number of decodings starting from i+2 to dp[i].
                dp[i] += dp[i + 2]
        
        # The result is the number of ways to decode the entire string, which is stored in dp[0].
        return dp[0]