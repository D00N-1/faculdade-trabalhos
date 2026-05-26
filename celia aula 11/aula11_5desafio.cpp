#include <iostream>
#include <string>
using namespace std;

class Produto {
private:
    string nome;
    double preco;
    int estoque;

public:
    Produto(string n, double p, int e) {
        nome = n;
        preco = p;
        estoque = e;
    }

    void mostrarProduto() {
        cout << "\nProduto: " << nome << endl;
        cout << "Preco: R$ " << preco << endl;
        cout << "Estoque: " << estoque << " unidades" << endl;
    }

    void vender(int quantidade) {
        if (quantidade <= estoque) {
            estoque -= quantidade;
            cout << quantidade << " unidade(s) vendida(s)." << endl;
        } else {
            cout << "Estoque insuficiente!" << endl;
        }
    }

    void adicionarEstoque(int quantidade) {
        estoque += quantidade;
        cout << quantidade << " unidade(s) adicionada(s)." << endl;
    }
};

int main() {
    Produto produto1("Dipirona", 8.50, 20);

    produto1.mostrarProduto();

    produto1.vender(5);
    produto1.adicionarEstoque(10);

    produto1.mostrarProduto();

    return 0;
}