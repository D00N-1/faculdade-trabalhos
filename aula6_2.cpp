#include <iostream>
using namespace std;

int main() {
    int num;

    cout << "Digite um numero para ver a tabuada: ";
    cin >> num;
    cout << "Tabuada de " << num << ":" << endl;

  
    for(int i = 1; i <= 10; i++) {
        cout << num << " x " << i << " = " <<  num * 1 << endl;
    }

    return 0;
}