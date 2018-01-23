#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <cstdlib>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
    double tmp_n,tmp_v;
    vector<double> norm = vector<double>(100,0);
    vector<double> val = vector<double>(100,0);
	int mult=1;
	int iter;
    ifstream input(argv[1],ios::in);
	if (argc > 2)
		mult = atoi(argv[2]);
    string s;
	cout << "nb_iter\t rel_res_norm\t time\n";
    while (input >> s)
    {
        if (s == "Initial")
        {
	    while (input >> s)
	    {
		if (s == "Cycle") {
                    input >> iter;
                    input >> s >> s >> tmp_n >> tmp_v;
                    norm[iter-1]+=tmp_n;
                    val[iter-1]+=tmp_v;
                    //cout << mult*iter << "\t " << norm << "\t " << val/10 << "\n";
	        } else if (s == "Number")
                    break;
	    }
        }
    }
    for (int i=0; i<50; i++)
    {
        norm[i]/=100;
        val[i]/=100;
        if (i>0)
            val[i] += val[i-1];
        cout << i+1 << "\t " << norm[i] << "\t " << val[i]/1000 << "\n";
    }
    input.close();
}
