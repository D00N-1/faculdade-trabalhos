#include <iostream>
#include <string>
using namespace std;

class veiculo {
    public:

 virtual void exibirInformacoes() const = 0; 
        
 virtual ~veiculo() {}
};

class Carro : public veiculo {
    public:
    void exibirInformacoes() const override {
        cout << "Carro: fusca azul" << endl;
    }
};

class Moto : public veiculo {
    public:
    void exibirInformacoes() const override {
        cout << "Moto: cg 160 peta" << endl;
    }
};

int main(){

    veiculo* v1 = new Carro();
    veiculo* v2 = new Moto();

    v1->exibirInformacoes();
    v2->exibirInformacoes();

    delete v1;
    delete v2;
    return 0;
}