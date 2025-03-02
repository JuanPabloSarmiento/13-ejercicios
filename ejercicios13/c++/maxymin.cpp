#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int a,b,c,d,e;
    cout << "digite 5 numeros \n";
    cin >> a >> b >> c >> d >> e;
    // se anidan varios max para descubrir el mayor de 5 numeros
    cout << "el mayor es : " << max(a,max(b,max(c,max(d,e))));
    return 0;
}