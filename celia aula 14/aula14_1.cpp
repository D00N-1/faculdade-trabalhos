#include <iostream>
using namespace std;

class energia {
public:
    void ligar() {
        cout << "Energia ligada!" << endl;
    }
    void desligar() {
        cout << "Energia desligada!" << endl;
    }
};

class seguranca {
public:
    void monitorar() {
        cout << "Seguranca monitorada!" << endl;
    }
};

class casainteligente : public energia, public seguranca {
public:
    void status() {
        cout << "Casa inteligente acionada!" << endl;
    }
};

int main() {
    casainteligente casa;

    casa.status();
    casa.ligar();
    casa.monitorar();
    
    return 0;
}