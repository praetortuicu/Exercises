#include <vector>
#include <iostream>



int removeElement(std::vector<int> &nums1, int &val) {
	int count = 0;
	int length = nums1.size();
	int iter = 0;
	while (iter != length) {
	   if (nums1[iter] == val) {
		count++;
	   } else if (count != 0){
		nums1[iter - count] = nums1[iter];
		if (iter != length - 1){
		    nums1[iter] = nums1[iter + 1];
		}
	   } 
	   iter++;
	}
	std::cout << "\n k = " << length - count << "\n";
	return length - count;
}



int main () {
    
    std::vector<int> nums1 = {1, 2, 2, 3};
    int val = 2;    
    std::vector<int> nums2 = {1, 2, 2, 2, 3, 2, 5, 9, 4, 4, 0};
    int val1 = 2;
    // removeElement(nums1, val);
    removeElement(nums2, val1);
    for (auto n : nums2) 
	    std::cout << n << " ";    
    return 0;
}
