#include <iostream>

using namespace std;

int main()
{
    int H, M, S, T, total;
    cin >> H;
    cin >> M;
    cin >> S;
    cin >> T;

    total = H * 3600 + M * 60 + S + T;

    (total / 3600 >= 24) ? cout << (total / 3600) % 24 << endl : cout << total / 3600 << endl;
    cout << (total % 3600) / 60 << endl;
    cout << total % 60;

    return 0;
}