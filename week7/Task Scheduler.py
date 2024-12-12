class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Figure out the frequencies
        task_counts = Counter(tasks)
        
        # Find the maximum frequency
        max_freq = max(task_counts.values())
        
        # Count how many tasks have the maximum frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Calculate the minimum number of time slots needed
        # Formula: (max_freq - 1) * (n + 1) + max_count
        # (max_freq - 1) is the number of "full cycles" 
        # (n + 1) represents the length of each cycle
        idle_slots = (max_freq - 1) * (n + 1) + max_count
        
        return max(idle_slots, len(tasks))