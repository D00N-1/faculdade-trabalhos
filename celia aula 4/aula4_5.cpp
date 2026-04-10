#include <iostream> 
using namespace std;

int main() {
    int k = 10, j = 10;
  
    k = k + 1;
    cout << "O valor de k alterado para " << k << "\n";
 
    j = j - 1;
    cout << "O valor de j alterado para " << j << "\n";
    
    k++;
    cout << "O valor de k alterado para " << k << "\n";
 
    j--;
    cout << "O valor de j alterado para " << j << "\n";
    
    ++k;
    cout << "O valor de k alterado para " << k << "\n";

    --j;
    cout << "O valor de j alterado para " << j << "\n";
    return 0;
}
