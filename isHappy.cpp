#include <iostream>
#include <array>

int digitSumSquare (int &num) {
    unsigned int sum = 0;
    while (num > 0) {
	sum += (num % 10) * (num % 10);
	std::cout << num % 10 << "**2 + " ;
	num /= 10;
    } 
    std::cout << " = " << sum << "\n";
    return sum;
}

bool isHappy(int &n) {
    int happySum = digitSumSquare(n);
    unsigned int count = 0;

    while (happySum > 1 && count < 100) {
	happySum = digitSumSquare(happySum);
	count++;
    }

    if (happySum == 1 && count < 100) {
	return true;
    } else {
	return false;
    }
}



int main() {
    int n = 19;
    isHappy(n);
    int n1 = 2;
    isHappy(n1);
    return 0;
}
