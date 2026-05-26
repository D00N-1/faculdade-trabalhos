#include <iostream>
#include <string>
using namespace std;

class contabancaria {
private:
    string titular;
    double saldo;

public:
    contabancaria() {
        saldo = 0;
    }

    void setTitular(string nome) {
        titular = nome;
    }

    string getTitular() {
        return titular;
    }

    void depositar(double valor) {
        saldo += valor;
        cout << "Depósito realizado com sucesso!" << endl;
    }

    void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
            cout << "Saque realizado!" << endl;
        } else {
            cout << "Saldo insuficiente!" << endl;
        }
    }

    double getSaldo() {
        return saldo;
    }
};

int main() {
    contabancaria conta;

    conta.setTitular("Maria");

    conta.depositar(1000);
    cout << "Titular: " << conta.getTitular() << endl;
    cout << "Saldo: R$ " << conta.getSaldo() << endl;

    conta.depositar(500);
    cout << "Saldo: R$ " << conta.getSaldo() << endl;

    conta.sacar(200);
    cout << "Saldo: R$ " << conta.getSaldo() << endl;

    conta.sacar(2000);
    cout << "Saldo: R$ " << conta.getSaldo() << endl;

    return 0;
}