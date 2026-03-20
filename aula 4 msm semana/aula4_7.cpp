#include <iostream>
using namespace std;

int main () {
    int precoProdutoA = 10;
    int precoProdutoB = 2;
    int temp = 0;

    cout << "Preco do Produto A = R$ " << precoProdutoA << "\n";
    cout << "Preco do Produto B = R$ " << precoProdutoB << "\n";

    cout << "\nTrocando os precos dos produtos...\n";

    temp = precoProdutoA;
    precoProdutoA = precoProdutoB;
    precoProdutoB = temp;

    cout << "\nNovo preco do Produto A = R$ " << precoProdutoA << "\n";
    cout << "Novo preco do Produto B = R$ " << precoProdutoB << "\n";

    return 0;
}