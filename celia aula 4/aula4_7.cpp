#include <iostream>
using namespace std;

int main()
{ 
    int x = 35, y = 2, z = 0;

    cout << "O valor de x = " << x << "\n";
    cout << "O valor de y = " << y << "\n";

    cout << "Troquei valores\n";

    z = y;
    y = x;
    x = z;

    cout << "O valor de x = " << x << "\n";
    cout << "O valor de y = " << y << "\n";

    x = x * -1;

    cout << "O valor de x negativo = " << x << "\n";

    return 0;
}