#include <iostream>
#include <algorithm>

using namespace std;

void sort(int array[], int size);

int main()
{
    int K, N;
    cin >> N >> K;
    int array[N];
    for (int i = 0; i < N; i++)
    {
        cin >> array[i];
    }

    sort(array, N);

    cout << array[K-1];

    return 0;
}

void sort(int array[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (array[j] < array[j+1]) {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}
