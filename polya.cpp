/*
 Author: Jayant Gupta
 Date: Dec 27. 2013
 In this program I have simulated polya's urn, this is an iterative process and the output distributions become more accurate
 as the number of iterations increase.
 ideal  no. of iterations is : 10000. here, represented by variable count.

 */

#include<iostream>
#include<vector>
#include<stdlib.h>

using namespace std;

// # red (1) balls = a ;
// #green (0) balls = b ;

// c = # of balls added after each iteration.
// n = # of times sampling is done based upon which y is calculated. 

int main(){
	int a, b, c, n; // standard polya's urn parameter.
	int count;
	cout << "give parameter a : "; cin >> a;
	cout << "give parameter b : "; cin >> b;
	cout << "give paramenter c : "; cin >> c;
	cout << "give parameter n : "; cin >> n;
	//n=a+b;
	cout << "give iteration count : "; cin >> count;
	int i, j; // iterators
	int val;
	int y;
	double occurence[n+1];
	for(i=0;i<=n;i++){
		occurence[i]=0;
	}
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
		occurence[y]++;
		//cout << (i+1) << " " << y << endl;
	}
	for(i=0;i<=n;i++){
		cout << "[" << i << ":" << occurence[i]/count << "] ";
	}
	cout << endl;
	//cout << endl;
}
