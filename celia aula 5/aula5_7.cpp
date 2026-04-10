#include <iostream>
using namespace std;

int main()
{
    char tamanho;
    float imc;
    cout << "Digite seu IMC: ";
    cin >> imc;
    cout << "Digite o tamanho (P/M/G): ";
    cin >> tamanho;
    tamanho = toupper(tamanho);

    switch (tamanho)
    {
    case 'P':
        cout << "Tamanho escolhido: Pequeno\n";
        if (imc >= 18 && imc <= 24)
        {
            cout << "Para este IMC, sugiro tamanho M\n";
        }
        break;

    case 'M':
        cout << "Tamanho escolhido: Medio\n";
        break;

    case 'G':
        cout << "Tamanho escolhido: Grande\n";
        break;

    default:
        cout << "Nao atendemos este publico\n";
    }

    return 0;
}