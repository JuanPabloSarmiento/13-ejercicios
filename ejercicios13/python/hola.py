print('- Hola mundo \n- Hoy es 10 de febrero de 2025 \n- Ficha 3066478');
nombre = str(input("ingrese su nombre "));
apellido = str(input("ingrese su apellido "));
nombreCompleto = {
    "nombre": nombre,
    "apellido": apellido
}
print(f"aprendiz{nombreCompleto}")
a = int(input("ingrese el primer numero:  "));
b = int(input("ingrese el segundo numero:  "));
print(f" El resultado de la suma es: {a + b}\n El resultado de la resta: {a - b}\n El resultado de la multiplicacion es: {a * b}\n El resultado de la division es: {a / b}\n El resultado de la potenciacion es: {a ** b}\n El porcentaje es {(a / b) * 100}\n El resultado de la raiz  es {a ** (1/b)} ");
print(f"a es menor que b {a < b}");
print(f"a es mayor que b {a > b}");
print(f"a es igual a b {a==b}");





