#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int N, cal = 0; 
    cin >> N;
    vector<int> array(N);
    for (int i = 0; i < N; i++){
        int a = 0;
        cin >> a;
        if (a == 0){
            if (!array.empty()){
                array.pop_back();
            }
        }
        else{
            array.push_back(a);
        }
    }

    for (int i = 0; i < array.size(); i++){
        cal += array[i];
    }
    cout << cal;
    
    return 0;
}

