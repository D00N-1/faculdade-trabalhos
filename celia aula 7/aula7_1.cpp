#include <iostream>
using namespace std;

int main() {
    float lado, areaq, base, altura, arear;

    cout << "Digite o lado do quadrado (entre 1 e 50): ";
    cin >> lado;

    if (lado < 1 || lado > 50) {
        cout << "Valor invalido! Digite entre 1 e 50.\n";
    } else {
        areaq = lado * lado;
        cout << "A area do quadrado é: " << areaq << endl;
    }

    cout << "----------------------------------" << endl << endl;

    cout << "Digite a base do retangulo (entre 1 e 50): ";
    cin >> base;

    cout << "Digite a altura do retangulo (entre 1 e 50): ";
    cin >> altura;

    if ((base < 1 || base > 50) || (altura < 1 || altura > 50)) {
        cout << "Valores invalidos! Digite entre 1 e 50.\n";
    } else {
        arear = base * altura;
        cout << "A area do retangulo é: " << arear << endl;
    }

    cout << "----------------------------------" << endl << endl;

    return 0;
}