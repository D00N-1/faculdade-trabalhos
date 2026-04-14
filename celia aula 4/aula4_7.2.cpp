#include <iostream>
using namespace std;

int main(){ 
    int x = 35, y = 2, z;

    cout << "Pedido original:\n";
    cout << "Hamburguer (x) = " << x << "\n";
    cout << "Batata (y) = " << y << "\n\n";

    cout << "O atendente vai trocar os pedidos ...\n";

    
    z = x; 
    x = y; 
    y = z; 

    cout << "\nPedido depois da troca:\n";
    cout << "Hamburguer (x) = " << x << "\n";
    cout << "Batata (y) = " << y << "\n";

    return 0;
}
