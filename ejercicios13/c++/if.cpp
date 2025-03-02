#include <iostream>
using namespace std;

int main (){
    int numero;
    cout << "digite un numero: \n " ;
    cin >>numero;
    if (numero > 0){
        cout << "el numero es positivo \n" ;
    } else if (numero == 0) {
        cout << "el numero es 0 \n";
    } else {
        cout << "el numero es negativo \n";
    }
    return 0;
}