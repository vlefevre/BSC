#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main(int argc, char **argv)
{
	ifstream input(argv[1],ios::in);
	string tmp;
	while (input >> tmp)
		if (tmp != "Initial")
			break;
	input >> tmp >> tmp;
	int precision;
	input >> precision;
	
	//READ PRECISION AND COUNT TIME WITH time(prec,alpha)

	return 0;
}

double time(int prec, double alpha)
{
	return pow((double)prec/32.,alpha);
}
