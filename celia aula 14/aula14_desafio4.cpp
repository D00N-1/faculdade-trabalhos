#include <iostream>
using namespace std;

// --- CLASSE BASE 1 ---
class ControleRemoto {
public:
    void controlarVoo() {
        cout << "Controlando o voo do drone..." << endl;
    }

    void ativar() {
        cout << "Controle remoto conectado." << endl;
    }
};

// --- CLASSE BASE 2 ---
class CameraAerea {
public:
    void gravarVideo() {
        cout << "Gravando video em alta resolucao." << endl;
    }

    void ativar() {
        cout << "Camera aerea iniciada." << endl;
    }
};

// --- CLASSE DERIVADA ---
class DroneInteligente : public ControleRemoto, public CameraAerea {
public:
    // Sobrescrita (Overriding)
    void ativar() {
        cout << "Drone realizando verificacoes de seguranca..." << endl;
    }
};

// --- FUNCAO PRINCIPAL ---
int main() {
    DroneInteligente drone;

    // Metodo da classe derivada
    drone.ativar();
    cout << "---------------------------------------" << endl;

    // Metodos das classes base
    drone.ControleRemoto::ativar();
    drone.CameraAerea::ativar();
    cout << "---------------------------------------" << endl;

    // Metodos exclusivos
    drone.controlarVoo();
    drone.gravarVideo();

    return 0;
}