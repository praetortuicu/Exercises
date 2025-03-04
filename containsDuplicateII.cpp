#include <iostream>
#include <vector>
#include <unordered_map>

bool containsDuplicateII(std::vector<int> &nums, int k) {
	std::unordered_map<int, int> index_map; // Stores number → last seen index

	    for (int i = 0; i < nums.size(); i++) {
		if (index_map.count(nums[i]) && (i - index_map[nums[i]]) <= k) {
		    return true;  // Found a duplicate within range k
		}
		index_map[nums[i]] = i;  // Update last seen index
	    }

	    return false;
}




int main () {
	std::vector<int> nums = {1, 2, 3, 1};
	int k = 3;
	std::vector<int> nums1 = {1, 2, 3, 1, 2, 3};
	int k1 = 2;
	containsDuplicateII(nums, k);
	containsDuplicateII(nums1, k1);
    return 0;
}
