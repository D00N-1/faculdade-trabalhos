#include <iostream>
using namespace std;

void menu() {
    cout << "Que periodo do dia está:\n";
    cout << "1 - Manha\n";
    cout << "2 - Tarde\n";
    cout << "3 - Noite\n";
    cout << "Digite a opcao: ";
}

void boas_vindas() {
    int op;
    cin >> op;

    if (op == 1) {
        cout << "Bom dia!" << endl;
    } else if (op == 2) {
        cout << "Boa tarde!" << endl;
    } else if (op == 3) {
        cout << "Boa noite!" << endl;
    } else {
        cout << "Periodo invalido!" << endl;
    }
}

int main() {
    menu();
    boas_vindas();
    cout << "encerrando\n";
    return 0;
}