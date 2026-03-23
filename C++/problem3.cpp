#include <iostream>
using namespace std;

int calculo(int D, int A, int N);

int main()
{
    int D, A, N;
    cin >> D;
    cin >> A;
    cin >> N;

    cout << calculo(D, A, N);

    return 0;
}

int calculo(int D, int A, int N)
{
    if (N == 1)
        return 31 * D;
    if (N > 1 && N < 16)
        return (31 - N + 1) * (D + (N - 1) * A);
    if (N >= 16)
        return 16 * (D + 14 * A);
}