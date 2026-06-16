#include <iostream>

class animal {
public:
    void respirar() { 
        std::cout << "Animal respirando!" << std::endl; 
    }
}; // <-- O erro estava aqui: faltava o ponto e vírgula

class reptil {
public:
    void rastejar() { 
        std::cout << "Reptil rastejando!" << std::endl; 
    }
};

class cobra : public animal, public reptil {
public:
    void respirar() { 
        std::cout << "Cobra respirando!" << std::endl; 
    }
};

int main() {
    cobra Cobra;

    Cobra.respirar();         // Chama o método da classe cobra (sobrescrito)
    Cobra.animal::respirar(); // Chama o método original da classe animal
    Cobra.rastejar();         // Chama o método da classe reptil (simplificado)

    return 0;
}