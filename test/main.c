#include <stdio.h>
#include <stdlib.h>
#include <mpfr.h>

void myprint(float n)
{
	printf("%f\n",n);
}

int main(int argc, char** argv)
{
	printf("Hello world\n");
	mpfr_t i,j,d;
	mpfr_init2(i,100);
	mpfr_set_d(i,1.0,MPFR_RNDD);
	mpfr_out_str(stdout,10,100,i,MPFR_RNDD);
	putchar('\n');
	mpfr_init2(d,100);
	mpfr_set_ui(d,48,MPFR_RNDD);
	mpfr_out_str(stdout,10,100,d,MPFR_RNDD);
	putchar('\n');
	mpfr_div(i,i,d,MPFR_RNDD);
	mpfr_out_str(stdout,10,0,i,MPFR_RNDD);
	putchar('\n');
	mpfr_init2(j,100);
	mpfr_set_d(j,1./48.,MPFR_RNDD);
	mpfr_out_str(stdout,10,0,j,MPFR_RNDD);
	putchar('\n');

	double r = 1.;
	myprint(r);
	if (r==1)
		printf("ok");
	else
		printf("mdr");
		printf("lol");
	return 0;
}
