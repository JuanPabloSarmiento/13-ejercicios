let apellido = "Sarmiento";
let edadPersona = 25;
let mayoriaDeEdad = true
// Si la edadPersona es mayor a 18, el usuario es mayor de edadPersona
if (edadPersona>18) {
    mayoriaDeEdad = true
}
else {
        mayoriaDeEdad = false
}

if (mayoriaDeEdad === true) {
    document.write(`Hola ${apellido} usted es mayor de edad`) 
}
else {
    document.write(`Hola ${apellido} usted no es mayor de edad`)
}