#include <iostream>
#include <string>
using namespace std;

class TrataDivZero
{
public:
    TrataDivZero(int n);
    void Msg();

private:
    int NLinha;
};

TrataDivZero::TrataDivZero(int n)
{
    NLinha = n; 
}

void TrataDivZero::Msg()
{
    cout << "Tratador de erro foi chamado..." << endl;
    cout << "Erro na linha: " << NLinha << endl;
}

int main()
{
    int n, m;

    cout << "Numerador: ";
    cin >> n;

    cout << "Denominador: ";
    cin >> m;

    try // inicio do try
    {
        if (m == 0)
        {
            throw TrataDivZero(__LINE__);
        }

        cout << "Divisao: " << (double)n / m << endl;
    }
    catch (TrataDivZero T)
    {
        T.Msg();
    }
    catch (bad_alloc &E) 
    {
        cout << "Faltou memoria...\n";
    }

    cout << "Fim..." << endl;

    return 0;
}