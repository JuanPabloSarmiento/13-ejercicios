def operaciones(num1,num2,operador):
    match operador:
        case "1":
            return "el resultado es", num1 + num2
        case "2":
            return "el resultado es",  num1 - num2
        case "3":
            return "el resultado es",  num1 * num2
        case "4":
            if num2==0:
                return "error: no se puede dividir por 0"
            else:
                return "el resultado es",  num1 / num2
        case _:
             "Operador invalido"
       
operacion = input("que operacion desea realizar:\n------ \n --------\n 1. suma \n 2. resta \n 3.multiplicacion \n 4. division \n ------ \n --------\n ")
a = int(input("digite el primer numero: "));
b = int(input("digite el segundo numero: "));
print(operaciones(a,b,operacion));