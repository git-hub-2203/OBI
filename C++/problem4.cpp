#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    vector<int> array(3);
    for (int i = 0; i < 3; i++){
        cin >> array[i];
    }
    sort(array.begin(), array.end());

    cout << array[1];

    return 0;
}
