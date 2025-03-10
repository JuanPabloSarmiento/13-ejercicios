#include <iostream>
using namespace std;
int main() {
    int a, b, op;
    cout << "1.Suma 2.Resta: "; cin >> op;
    cout << "Ingrese dos números: "; cin >> a >> b;
    switch(op) { case 1: cout << (a + b); break; case 2: cout << (a - b); break; }
    return 0;
}