#include <iostream>
using namespace std;

// ===== CLASSE PILHA =====
class MinhaPilha {
private:
    int vetor[5];
    int topo;

public:
    MinhaPilha() {
        topo = -1;
    }

    void adicionar(int valor) {

        if (topo >= 4) {
            cout << "Pilha lotada!" << endl;
        }
        else {
            topo++;
            vetor[topo] = valor;
        }
    }

    void exibir() {

        cout << "\nElementos da Pilha:\n";

        for (int i = topo; i >= 0; i--) {
            cout << vetor[i] << endl;
        }
    }
};

// ===== CLASSE FILA =====
class MinhaFila {
private:
    int vetor[5];
    int fim;

public:
    MinhaFila() {
        fim = -1;
    }

    void inserir(int valor) {

        if (fim >= 4) {
            cout << "Fila lotada!" << endl;
        }
        else {
            fim++;
            vetor[fim] = valor;
        }
    }

    void exibir() {

        cout << "\nElementos da Fila:\n";

        for (int i = 0; i <= fim; i++) {
            cout << vetor[i] << endl;
        }
    }
};

// ===== MAIN =====
int main() {

    MinhaPilha pilha;
    MinhaFila fila;

    int valor;

    cout << "Digite 5 numeros:\n";

    for (int i = 0; i < 5; i++) {

        cin >> valor;

        pilha.adicionar(valor);
        fila.inserir(valor);
    }

    fila.exibir();
    pilha.exibir();

    return 0;
}