class Banco:
    def __init__(self, usuario, pin, saldo):
        self.usuario = usuario
        self.pin = pin
        self.saldo = saldo

    def autenticar(self,usuario,pin):
        if usuario == self.usuario and pin == self.pin:
            print("estas logeado")
        opciones = int(input("seleccione \n 1. consultar \n 2. retirar"))
        if opciones == 1:
            print(self.saldo)
        elif opciones ==2 :
            retirar()

    def consultar(self):
            if usuario == self.usuario and pin == self.pin:
                print(f"su saldo es {self.saldo}")
    
    def retirar(self):
            if usuario == self.usuario and pin == self.pin:
                retiro = int(input(f"su saldo es {self.saldo} ¿cuanto desea retirar?  "))
                if retiro <= self.saldo:
                    self.saldo -= retiro
                    print(f"Usted ha retirado {retiro} su nuevo saldo es {self.saldo} \n  GRACIAS POR SU VISITA")
                else: print("saldo insuficiente")
            else: print("usuario o contraseña incorrectos")

usuario1 = Banco("pepe","4323",2000);
usuario2 = Banco("ana", "1234", 5000);
usuario3 = Banco("carlos", "5678", 1500);
usuario4 = Banco("maria", "9876", 3200);
usuario5 = Banco("jose", "1111", 2800);
usuario6 = Banco("laura", "2222", 4500);
usuario7 = Banco("daniel", "3333", 3700);

clientes = [usuario1,usuario2,usuario3,usuario4,usuario5,usuario6,usuario7]


usuario = input("digite su usuario: ")
if usuario in [clientes]:
    usuario.autenticar()
else: print("no se encuentra")




