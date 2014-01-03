#include<iostream>
#include<vector>
#include<stdlib.h>

using namespace std;

// # red (1) balls = a ;
// #green (0) balls = b ;

int main(){
	int a, b, c, n; // standard polya's urn parameter.
	int count;
	cout << "give parameter a : "; cin >> a;
	cout << "give parameter b : "; cin >> b;
	cout << "give paramenter c : "; cin >> c;
	cout << "give parameter n : "; cin >> n;
	cout << "give iteration count : "; cin >> count;
	int i, j; // iterators
	int val;
	int y;
	for(i=0 ; i<count ; i++){
		y=0; // counts the number of red occurences.
		for(j=0 ; j<n ; j++){
			val = rand() % (a+b);
			if(val < a){
				a+=c;
				y++;
			}
			else{
				b+=c;
			}
		}
		cout << (i+1) << " " << y << endl;
	}
	//cout << endl;
}
