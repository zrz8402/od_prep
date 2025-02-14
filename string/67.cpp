#include <iostream>
#include <bitset>
#include <cmath>

using namespace std;

string addBinary(string a, string b) {
    int sum = stoi(a, nullptr, 2) + stoi(b, nullptr, 2);
	if (sum == 0)
		return "0";
    return bitset<32>(sum).to_string().substr(32 - ceil(log2(sum + 1)));
}

int main() {
    cout << addBinary("1101", "1101") << endl;
    cout << addBinary("0", "1") << endl;
}
