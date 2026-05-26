#include <iostream>
using namespace std;

class Funcionario {
protected:
    double salario;

public:
    Funcionario(double s) {
        salario = s;
    }

    virtual double calcularSalario() {
        return salario;
    }
};

class Gerente : public Funcionario {
public:
    Gerente(double s) : Funcionario(s) {}

    double calcularSalario() override {
        return salario + 1000;
    }
};

class Vendedor : public Funcionario {
public:
    Vendedor(double s) : Funcionario(s) {}

    double calcularSalario() override {
        return salario + 500;
    }
};

int main() {
    Gerente g(3000);
    Vendedor v(1800);

    cout << "Salario gerente: R$ " << g.calcularSalario() << endl;
    cout << "Salario vendedor: R$ " << v.calcularSalario() << endl;

    return 0;
}