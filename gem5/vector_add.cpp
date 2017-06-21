#include <iostream>
#include <vector>

using namespace std;

int main() {
	vector<double> v;
	for (int i=0; i<100; i++)
	{
		v.push_back((double)(i+1)/20.);
	}
	double total = 0;
	for (int i=0; i<100; i++)
	{
		total += v[i];
	}
	cout << total << "\n";
	return 0;
}
