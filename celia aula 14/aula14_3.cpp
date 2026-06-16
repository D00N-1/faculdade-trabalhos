#include <iostream>
using namespace std;

class presenca {
public:
    void registrarpresenca() {
        cout << "Presenca registrada!" << endl;
    }

    void status() {
        cout << "Status de presenca: presente!" << endl;
    }
};

class avalicao {
public:
    void lancarnota() {
        cout << "Nota lancada!" << endl;
    }
    
    void status() {
        cout << "Status de avaliacao: nota lancada!" << endl;
    }
}; // <-- Correção 1: Faltava fechar a classe 'avalicao' aqui

class aluno : public presenca, public avalicao {
public:
    void status() {
        cout << "Dados academicos do aluno atualizados!" << endl;
    }
};

int main() {
    aluno Aluno;

    Aluno.status();           // Chama o método da classe aluno (sobrescrito)
    Aluno.presenca::status(); // Chama o método da classe presenca
    Aluno.avalicao::status(); // Chama o método da classe avalicao

    Aluno.registrarpresenca(); // <-- Correção 2: Maiúscula (Objeto 'Aluno', não a classe 'aluno')
    Aluno.lancarnota();        // <-- Correção 2: Maiúscula (Objeto 'Aluno', não a classe 'aluno')

    return 0;
}