#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main(void){
	int T;
	double A;
	cin >> T;
	for (int i=0; i<T; i++){
		cin >> A;
		double angle;
		angle=acos(A*sqrt(2)/2) - (M_PI) /4;
		double mprosta_x;
		mprosta_x=-0.5 * sin(angle);
		double mprosta_y=0.5*cos(angle);
		double mprosta_z=0.5;

		double dexi_x=0.5 * cos(angle);
		double dexi_y=0.5 * sin(angle);
		double dexi_z=0;
		cout << "Case #" << (i+1) <<":" << endl;
		cout << "0 0 0.5" << endl;
		cout << mprosta_x << " " << mprosta_y << " " << mprosta_z << endl;
		cout << dexi_x << " " << dexi_y << " " << dexi_z << endl;
	}
}