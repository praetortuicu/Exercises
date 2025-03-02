#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSumOptimized(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> num_indices;

    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (num_indices.find(complement) != num_indices.end()) {
            return {num_indices[complement], i};
        }
        num_indices[nums[i]] = i;
    }

    return {};
}

std::vector<int> twoSum (std::vector<int> &nums, int target) {
    std::vector<int> result(2, -1);

    // int length = nums.size();
    int sum = 0;

    for (int i = 0; i < nums.size(); i++) {
	for (int j = i + 1; j < nums.size(); j++) {
	    sum = nums[i] + nums[j];
	    if (sum == target) {
		result[0] = i;
		result[1] = j;	
	    }
	}
    }

    if (sum == 0) { std::cout << "something went wrong!"; }
    std::cout << result[0] << " " << result[1] << "\n";
    return result;
}


int main() {
    std::vector<int> nums = {1, 2, 3};
    int target = 5;
    twoSum(nums, target);

    return 0;
}
