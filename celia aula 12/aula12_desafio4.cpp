#include <iostream>
#include <string>
using namespace std;

class Pessoa {
private:
    string nome;
    string sobrenome;
    int idade;
    string genero;
    bool dormindo;

public:
    Pessoa(string n, string s, int i, string g) {
        nome = n;
        sobrenome = s;
        idade = i;
        genero = g;
        dormindo = false;
    }

    void mostrarDados() {
        cout << "Nome: " << nome << " " << sobrenome << endl;
        cout << "Idade: " << idade << endl;
        cout << "Genero: " << genero << endl;
    }

    void comer() {
        if (!dormindo) {
            cout << nome << " esta comendo." << endl;
        } else {
            cout << nome << " nao pode comer porque esta dormindo." << endl;
        }
    }

    void estudar() {
        if (!dormindo) {
            cout << nome << " esta estudando programacao." << endl;
        } else {
            cout << nome << " nao pode estudar dormindo." << endl;
        }
    }

    void dormir() {
        if (!dormindo) {
            dormindo = true;
            cout << nome << " foi dormir." << endl;
        } else {
            cout << nome << " ja esta dormindo." << endl;
        }
    }

    void acordar() {
        if (dormindo) {
            dormindo = false;
            cout << nome << " acordou." << endl;
        } else {
            cout << nome << " ja esta acordado." << endl;
        }
    }
};

int main() {
    Pessoa pessoa1("Carlos", "Oliveira", 22, "Masculino");

    cout << "--- Dados da Pessoa ---" << endl;
    pessoa1.mostrarDados();

    cout << "\n--- Acoes ---" << endl;
    pessoa1.comer();
    pessoa1.estudar();
    pessoa1.dormir();
    pessoa1.estudar();
    pessoa1.acordar();
    pessoa1.comer();

    return 0;
}
