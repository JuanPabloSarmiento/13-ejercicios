#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main(){
    //declarar variables a usar
    int edad;
    float altura;
    char inicial;
    bool estudiante;
    string respuesta;
    string apellido;
    
    // entrada de variables
    cout << "ingrese su edad: " ;
    cin >> edad ;
    cout << "ingrese su altura: ";
    cin >> altura;
    cout << "digite su inicial: ";
    cin >> inicial;
    cout << "es estudiante? true or false? : ";
    cin >> respuesta;
    cout << "ingrese su apellido: ";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    getline(cin,apellido);
    //definimos que variables dan como salida true
    estudiante = (respuesta == "true" || respuesta == "si");

    // damos enunciados
    cout << "su edad es de: " << edad << endl;
    cout << "su altura es de: " << altura << endl;
    cout << "su inicial es : " << inicial << endl;
    cout << "es estudiante? " << (estudiante ? "si": "no") << endl;
    cout << "su apellido es " << apellido << endl;
    return 0;
}