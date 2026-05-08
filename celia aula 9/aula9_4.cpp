#include <iostream>
#include <string>
using namespace std;

struct Pessoa {
    string nome;
    int idade;
    float altura;
};

int main() {
    char continuar = 's';

    while (continuar == 's' || continuar == 'S') {
        Pessoa p;

        cout << "Digite o nome: ";
        getline(cin, p.nome);

        cout << "Digite a idade: ";
        cin >> p.idade;

        cout << "Digite a altura (em metros): ";
        cin >> p.altura;

        cout << "\nInformacoes da Pessoa:" << endl;
        cout << "Nome: " << p.nome << endl;
        cout << "Idade: " << p.idade << " anos" << endl;
        cout << "Altura: " << p.altura << " metros" << endl;

        cout << "\nDeseja cadastrar outra pessoa? (s/n): ";
        cin >> continuar;

        cin.ignore(1000, '\n');
    }

    cout << "\nPrograma encerrado" << endl;

    return 0;
}