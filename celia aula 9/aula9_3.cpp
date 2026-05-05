#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct pessoa {
    string nome;
    int idade;
    float altura;
};

int main() {

    vector<pessoa> pessoas;
    char continuar = 's';

    while (continuar == 's' || continuar == 'S') {

        pessoa p;

        cin.ignore();

        cout << "Digite o nome: ";
        getline(cin, p.nome);

        cout << "Digite a idade: ";
        cin >> p.idade;

        cout << "Digite a altura (em metros): ";
        cin >> p.altura;

        pessoas.push_back(p);

        cout << "Deseja adicionar outra pessoa? (s/n): ";
        cin >> continuar;
    }

    cout << "\nLista de pessoas:\n";

    for (int i = 0; i < pessoas.size(); i++) {

        cout << "\nPessoa " << i + 1 << ":" << endl;

        cout << "Nome: " << pessoas[i].nome << endl;
        cout << "Idade: " << pessoas[i].idade << " anos" << endl;
        cout << "Altura: " << pessoas[i].altura << " m" << endl;
    }

    return 0;
}