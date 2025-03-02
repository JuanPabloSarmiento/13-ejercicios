class Banco {
    constructor(usuario,pin,saldo) {
        this.usuario = usuario;
        this.pin = pin;
        this.saldo = saldo;
    }
    ingresar(usuario,pin,saldo){
        let login = true;
        if(usuario == this.usuario && pin == this.pin){
            document.write(`${this.usuario} has ingresado <br>`)
            login = true;   
    }
        else {
            document.write("usuario o pin incorrecto")
           login = false;
        }
        }
        

    consultar(saldo){
        document.write(`Su saldo es : ${this.saldo} <br>`)
    }
    retirar(saldo){
        let retiro = parseInt(prompt("cuanto desea retirar"))
        if (retiro <= this.saldo) {
            this.saldo = this.saldo - retiro;
            document.write(`retiro exitoso <br> su saldo disponible es ${this.saldo}`)
        }
        else {
            document.write("saldo insuficiente")
        }
    }

}

const cliente1 = new Banco("Juan",2232,9050);
const cliente2 = new Banco("Jhon",8952,4500);

const clientes = [
     cliente1,
     cliente2
]

let ingresa = prompt("digite usuario")
let contraseña = parseInt(prompt("digite contraseña"))

let clienteEncontrado = clientes.find(element => ingresa === element.usuario && contraseña === element.pin);
if (clienteEncontrado) {
    clienteEncontrado.ingresar(ingresa,contraseña)
         let opciones = prompt(`digite la opcion : <br> 1.consultar <br> 2.retirar`) 
        if (opciones == 1){
            clienteEncontrado.consultar()
        }
        if (opciones == 2) {
            clienteEncontrado.retirar()
        }
}

