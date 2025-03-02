figura = input("digite la figura \n triangulo: T \n rombo: RO \n cuadrado: C \n rectangulo: REC \n cilindro: CIL \n")
pi = 3.14
match(figura):
    case "T": 
        base = int(input("digite la base "))
        altura = int(input("digite la altura "))
        resultado = (base*altura)/2;
        print(f"el area del triangulo es {resultado}")
    case "RO":
        base = int(input("digite la base "))
        altura = int(input("digite la altura "))
        resultado = base*altura;
        print(f"el area del rombo es {resultado}")
    case "C":
        base = int(input("digite la base "))
        altura = int(input("digite la altura "))
        resultado = base*altura;
        print(f"el area del cuadrado es {resultado}")
    case "REC":
        base = int(input("digite la base "))
        altura = int(input("digite la altura "))
        resultado = base*altura;
        print(f"el area del rectangulo es {resultado}")
    case "CIL":
        radio = int(input("digite el radio "))
        altura = int(input("digite la altura "))
        resultado1 = (2*pi*radio)**2
        resultado2 = 2*pi*radio*altura
        area = resultado1 + resultado2
        print(f"el area del cilindro es {area} ")
    case _: 
        print("no se reconoce la figura ")