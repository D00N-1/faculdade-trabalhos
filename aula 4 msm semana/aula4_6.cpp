#include <iostream>
using namespace std;

int main() 
{
    int n1;
    int n2 = 50, n3, x = 3, y = 4, i = 5;

    x += 3;

    x *= y + 1;

    x *= y++;

    y = ++i;

    cout << "Entre com um numero inteiro (n1): ";
    cin >> n1;

    n1 = n1 + n1 * 10;
    n2 = n1 / 5;
    n3 = n2 % 5 * 7;
    n2 *= n3-- % 4;

    cout << n2 << " " << n3 << " " << (n2 != n3 + 21) << endl;

    return 0;
}