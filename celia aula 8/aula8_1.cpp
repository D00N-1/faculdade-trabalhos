#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;
//float MEU_PI = 3.14

float areaQuadrado(float lado) {
     return lado * lado;
}

float areaRetangulo(float base, float altura) {
    float resultado =0;
    resultado = base * altura;
    return resultado;
}

float areaCirculo(float raio) {
    return M_PI * raio * raio;
}

void menu() {
    int opcao;

    cout << "===CALCULO DE AREAS===" << endl;
    cout << "1. Area do quadrado" << endl;
    cout << "2. Area do retangulo" << endl;
    cout << "3. Area do circulo" << endl;
    cout << "4. Sair" << endl;
    cout << "Escolha uma opcao: ";
    cin >> opcao;

    if (opcao == 1) {
        float lado;
        cout << "Digite o lado do quadrado: ";
        cin >> lado;
        cout << "Area do quadrado: " << areaQuadrado(lado) << endl;

    } else if (opcao == 2) {
        float base, altura;
        cout << "Digite a base: ";
        cin >> base;
        cout << "Digite a altura: ";
        cin >> altura;
        cout << "Area do retangulo: " << areaRetangulo(base, altura) << endl;
    } else if (opcao == 3) {
        float raio;
        cout << "Digite o raio do circulo: ";
        cin >> raio;
        cout << "Area do circulo: " << areaCirculo(raio) << endl;


} else {
        cout << "Opcao invalida. Saindo..." << endl;
    }
}

int main() {
    menu();
    return 0;
}