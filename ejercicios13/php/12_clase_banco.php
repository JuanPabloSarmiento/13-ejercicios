<?php
class Banco {
    private $usuario;
    private $saldo;

    public function __construct($usuario, $saldo) {
        $this->usuario = $usuario;
        $this->saldo = $saldo;
    }

    public function consultarSaldo() {
        return "Saldo actual: $" . $this->saldo;
    }

    public function retirar($monto) {
        if ($monto > $this->saldo) {
            return "Fondos insuficientes.";
        } else {
            $this->saldo -= $monto;
            return "Retiro exitoso. Nuevo saldo: $" . $this->saldo;
        }
    }
}

$miBanco = new Banco("Juan", 1000);
echo $miBanco->consultarSaldo();
echo "\n" . $miBanco->retirar(200);
?>