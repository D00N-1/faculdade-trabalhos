#include <iostream>
using namespace std;

int main() {
    int dia, op;

    cin >> dia;

    switch(dia) {
        case 1:
            cin >> op;
            switch(op) {
                case 1: cout << "R$15\n"; break;
                case 2: cout << "R$10\n"; break;
                default: cout << "Opcao invalida\n";
            }
            break;

        default:
            cout << "Dia invalido\n";
            break;
    }

    return 0;
}   