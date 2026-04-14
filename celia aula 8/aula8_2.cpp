#include <iostream>
using namespace std;

void menu() {
    cout << "1 - bermuda" << endl;
    cout << "2 - chinelo" << endl;
    cout << "Digite sua opcao: ";
}

float valores(int op) {
    float valor = 0; // inicializa

    switch (op) {
        case 1:
            valor = 20.0;
            break;
        case 2:
            valor = 10.0; // exemplo de valor para chinelo
            break;
        default:
            cout << "Nao existe essa opcao!" << endl;
            break;
    }

    return valor;
}

int main() {
    int op, qtd;
    float valor_individual, total;

    menu();
    cin >> op;

    cout << "Digite a quantidade: ";
    cin >> qtd;

    valor_individual = valores(op);

    total = valor_individual * qtd;

    cout << "Valor total: " << total << endl;

    return 0;
}