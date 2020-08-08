#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>


using namespace std;


int main(){
    int num;
    cin>>num;

    /*vector <float*> graph;
    for(int i=0;i<=num;i++){
        graph.push_back(new float[100001]);
    }*/
    float** graph = new float*[num+2];
    for(int i = 0; i < num+2; ++i)
        graph[i] = new float[num+2];
    for(int i=0;i<=num;i++){
        for(int j=0;j<=num;j++){
            graph[i][j]=0;
        }
    }

    int max, ans;
    max=-1;
    ans=-1;
    for(int i=1;i<num;i++){
        int n1, n2;
        float len;
        cin>>n1>>n2>>len;
        graph[n1][n2] = len;
        graph[n2][n1] = len;
        for(int j=1;j<num+1;j++){
            if(graph[j][n2]!=0 && j!=n1 && graph[j][n1] == 0){
                graph[j][n1] = graph[j][n2] + graph[n1][n2];
                graph[n1][j] = graph[n2][j] + graph[n1][n2];
                if(graph[j][n1]>max){
                    ans = max;
                    max = graph[j][n1];

                }
                else if(graph[j][n1]>ans){
                    ans = graph[j][n1];
                }

            }
            if(graph[j][n1]!=0 && j!=n2 && graph[j][n2] == 0){
                graph[j][n2] = graph[j][n1] + graph[n1][n2];
                graph[n2][j] = graph[n1][j] + graph[n1][n2];
                if(graph[j][n2]>max){
                    ans = max;
                    max = graph[j][n2];

                }
                else if(graph[j][n2]>ans){
                    ans = graph[j][n2];
                }
            }
        }
        
        if(len>max){
            ans = max;
            max = len;

        }
        else if(len>ans){
            ans = len;
        }       
    }
    cout<<ans;
}