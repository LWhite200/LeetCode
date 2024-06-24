class Solution {
public:
// example solution, not my own, new to this website and its 2am
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i<n-1; i++) {
            for (int j = i + 1; j < n; j++) {
                if(nums[i] + nums[j] == target)
                return {i, j};
            }
        }
        return {};
    }
};