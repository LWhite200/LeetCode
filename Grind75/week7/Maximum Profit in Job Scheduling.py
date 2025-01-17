" Simple Bottom Up DP solution "
" Python can easily create job 'objects' "
" Maximum Profit in Job Scheduling "

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted(zip(startTime, endTime, profit)) 
        numJobs = len(profit)
        
        dp = [0] * (numJobs + 1)
        
        def nextNon(i):
            s1, e1, p1 = jobs[i]
            left, right = i + 1, numJobs

            while left < right:
                mid = (left + right) // 2
                if jobs[mid][0] >= e1: 
                    right = mid
                else:
                    left = mid + 1
            return left
        
        for i in range(numJobs - 1, -1, -1):
            s1, e1, p1 = jobs[i]
            nextJob = nextNon(i)
            dp[i] = max(p1 + dp[nextJob], dp[i + 1])

        return dp[0]
