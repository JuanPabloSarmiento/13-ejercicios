#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main (){
    int a,b,c;
    string mayor;
    cout << "digite 3 numeros enteros \n";
    cin >> a >> b >> c;
    mayor = (a==b and b==c ? "son iguales" : a>b and a>c ? "el mayor es a" : b>a and b>c ? "el mayor es b" : "el mayor es c");
    cout << mayor << endl;  
    return 0;
}