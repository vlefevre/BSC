#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;
double alpha;

double time(int prec);

int main(int argc, char **argv)
{
	ifstream input(argv[1],ios::in);
	ofstream output(argv[2],ios::out);
	stringstream ss(argv[3]);
	ss >> alpha;
	string tmp;
	while (input >> tmp)
		if (tmp == "Initial")
			break;
	input >> tmp >> tmp;
	int precision;
	input >> precision;
	int iter;
	double rel_res_norm;
	double total_cost = 0;
	double cost;
	//READ PRECISION AND COUNT TIME WITH time(prec,alpha)
	input >> tmp;
	while (tmp == "Cycle")
	{
		input >> iter >> tmp >> tmp >> rel_res_norm;
		cost = time(precision);
		total_cost += cost;
		output << iter << " " << cost << " " << total_cost << " " << rel_res_norm << "\n";
		input >> precision;
		if (precision > 53) precision = 53;
		input >> tmp;
	}
	
	return 0;
}

double time(int prec)
{
	return pow((double)prec/53.,alpha);
}
