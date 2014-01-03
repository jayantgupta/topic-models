#include<stdio.h>
#include<stdlib.h>

double max(double a, double b){
	printf("(%f %f) ", a ,b);
	return a>b?a:b;
}

main(){
	int n;
	scanf("%d",&n);
	int i,j;
	int a[n];
	for(i=0 ; i<n ; i++){
		a[i] = 0;
	}
	double alpha = 1.2; // parameter : To regulate the probability of adding a new table for a new input.
	double pmax, pcurr;
	int tableNo, tableCount;
	pmax = pcurr = 0;
	tableCount = 0;
	int ntFlag;
	for(i=0;i<n;i++){
		tableNo = 0;
		ntFlag = 0;
		pmax = 0;
		for(j=0;j<tableCount;j++){
			if( (alpha/(i+alpha)) > (a[j]/(i+alpha)) && pmax < alpha/(i+alpha)){
				pmax = alpha/(i+alpha);
				ntFlag = 1;
			}
			else if(a[j]/(i+alpha) > pmax){
				pmax = a[j]/(i+alpha);
				ntFlag = 0;
				tableNo = j;
			}	
		}
		if(ntFlag == 1){
			tableNo = tableCount;
		       	tableCount++;
		}
		if(ntFlag == 0 && a[tableNo] == 0){
			tableCount++;
		}
		a[tableNo]++;
	}
	printf("No. of tables = %d\n",tableCount);
	for(i=0;i<tableCount;i++){
		printf("people at table %d = %d\n",i,a[i]);
	}
}
