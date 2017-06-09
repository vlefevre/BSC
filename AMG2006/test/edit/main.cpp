#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int main(int argc, char** argv)
{
    double norm = 0;
    double val = 0;
int	mult=1;
	int iter=1;
    ifstream input(argv[1],ios::in);
	if (argc > 2)
		mult = atoi(argv[2]);
    string s;
	cout << "nb_iter\t rel_res_norm\t time\n";
    while (input >> s)
    {
        if (s == "norm")
        {
            input >> s >> val;
            norm = val;
        } else if (s == "Multi-grid:")
        {
	    while (input >> s)
	    {
		if (s == "wall") {
                    input >> s >> s >> s >> val;
                    cout << mult*iter << "\t " << norm << "\t " << val/10 << "\n";
                    iter++;
		    break;
	        }
	    }
        }
    }
    input.close();
}
