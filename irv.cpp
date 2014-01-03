/*
	Instant Run-off Voting : (Independent Random Variable)
	In this case users rank the probable list of candidates. 
	Final output is calculated by user given the best rank by mof the people.

	Ballots are initially distributed based on each elector's first preference. 
	If a candidate secures more than half of votes cast, that candidate wins. Otherwise, 
	the candidate with the fewest votes is eliminated. Ballots assigned to the 
	eliminated candidate are recounted and assigned to those of the remaining 
	candidates who rank next in order of preference on each ballot. This process 
	continues until one candidate wins by obtaining more than half the votes.

*/
#include<iostream>
#include<vector>

using namespace std;

int getMaxIndex(int count [], int n){
	int i;
	int max=0;
	int index=0;
	for(i=0; i<n; i++){
		if(max < count[i]){
			max = count[i];
			index = i;
		}	
	}
	return index;
}

int getMinIndex(int count [], int n){
	int i;
	int min=1000 ; // always equal to maximum possible votes.
	int index=0;
	for(i=0; i<n; i++){
		if(min > count[i] && count[i]>0){
			min = count[i];
			index = i;
		}	
	}
	return index;
}

main(){
	int n; // no. of candidates.
	int i, vCount;
	cin >> n; //	scanf("%d",&n);
	vector<int> voteList[n];
	cin >> vCount;
	int votes[1000][n];
	int count[n];
	int vId=0; // voter ID;
	char c;
	for(vId=0; vId < vCount ; vId++){
		int rank; // rank starts from 1, ... , n;
		for(i=0; i<n ; i++){
			cin  >> rank;
			votes[vId][rank-1] = i;  // scanf("%d",&votes[vId][i]);
			if(rank == 1){
				count[i]++;
				voteList[i].push_back(vId);
			}
		}
		//vId++;
	}
	int j;
	/*for(i=0 ; i<vCount; i++){
		for(j=0 ; j<n ; j++){
			cout << votes[i][j] << " " ;
		}
		cout << endl;
	}*/
	cout << "votes submitted : " << vId << endl;
	int maxIndex = getMaxIndex(count, n);
	int minIndex = getMinIndex(count, n);
	//for(i=0;i<n;i++){
	//	cout << count[i] << endl;
	//}
	//cout << (vId/2) << endl;
	cout << "making decision" << endl;
	int candidate;
	int iteration = 1;
	
	while(count[maxIndex] < vId/2 && iteration < n ){
	//	cout << "here..." << endl;
		minIndex = getMinIndex(count, n);
	//	cout << count[minIndex] << endl;
		for(vector<int>::size_type i = 0 ; i<count[minIndex]; i++){ //voteList[minIndex].size() 
			vId = voteList[minIndex][i];
			candidate = votes[vId][iteration];
			voteList[candidate].push_back(vId); // adds the votes of the minimum voted candidate.	
			count[candidate]++;
	//		cout << vId << " " << candidate << " " << endl;
		}
		count[minIndex] = 0;		
		maxIndex = getMaxIndex(count, n);
		iteration++;
	}
	cout << "And the winner is candidate : " << maxIndex + 1 << endl;
}
