#include <iostream> //aprendendo vetor e matriz
using namespace std;
int main() {
    int vetor[5]; //declara um vetor de 5 posicoes
    int matriz[5][3]; //declara uma matriz de 5 linhas e 3 colunas
   
vetor[0] = 9; //coloca o 9 na primeira posicao do vetor
vetor[4] = 30; //coloca o 30 na ultima posicao do vetor

matriz[0][1] = 15; //coloca o 15 na celula que esta na primeira linha 
                   // e na segunda coluna da matriz

cout << "O Vetor na posicao 0 tem o valor: " << vetor[0];
return 0;
}   