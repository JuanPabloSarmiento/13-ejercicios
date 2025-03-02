datoRequerido = input("digite en mayuscula que dato necesita hallar: \n v : voltaje r \n r: resistencia \n I: intensidad. \n");
if datoRequerido == "V":
    resistencia = float(input("digite la resistencia: "));
    intensidad = float(input("digite la intensidad: "));
    resultado = resistencia*intensidad;
    print(f"el voltaje es : {resultado}");
if datoRequerido == "R":
    intensidad = float(input("digite la intensidad: "));
    voltaje = float(input("digite la voltaje: "));
    resultado = voltaje/intensidad;
    print(f"el voltaje es : {resultado}");
if datoRequerido == "I":
    resistencia = float(input("digite la resistencia: "));
    voltaje = float(input("digite la voltaje: "));
    resultado = voltaje/resistencia;
    print(f"el voltaje es : {resultado}");
else: print("el valor ingresado no es correcto");





