#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main(){
	int N;
	vector<float> dist1;
	vector<float> dist2;
	vector<int> Ax;
	vector<int> Ay;
	cin >> N;

	for(int i = 0; i < N; ++i){
		int x, y;
		cin >> x >> y;
		Ax.push_back(x);
		Ay.push_back(y);
	}

	int Xg, Yg, Xa, Ya;
	cin >> Xg >> Yg >> Xa >> Ya;
	
	for(int i = 0; i < N; ++i){
		dist1.push_back(pow(Xg - Ax[i], 2) + pow(Yg - Ay[i], 2));
		dist2.push_back(pow(Xa - Ax[i], 2) + pow(Ya - Ay[i], 2));
	}

	int Q;
	cin >> Q;

	for(int i = 0; i < Q; ++i){
		int Rg, Ra;
		cin >> Rg >> Ra;

		int num = 0;

		for(int j = 0; j < N; ++j){
			if(((dist1[j] > pow(Rg, 2)) && (dist2[j] > pow(Ra, 2))) || ((dist1[j] <= pow(Rg, 2)) && (dist2[j] <= pow(Ra,2)))){
				++num;
			}
		}
		cout << num << endl;
	}

}