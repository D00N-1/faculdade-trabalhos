#include <iostream>
using namespace std;

class animal {
    public:
    virtual void fazersom() = 0; 

};

class cachorro : public animal {
    public:
    void fazersom() override {
        cout << "Au Au!" << endl;
    }
};

class gato : public animal {
    public:
    void fazersom() override {
        cout << "miau!" << endl;
    }
};

int main() {
   cachorro c;
   gato g;

    c.fazersom();
    g.fazersom();

    return 0;
}