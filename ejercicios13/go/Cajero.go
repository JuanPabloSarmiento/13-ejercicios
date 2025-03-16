package main
import "fmt"
func main() {
    saldo := 1000
    var monto int
    fmt.Print("Ingrese monto a retirar: ")
    fmt.Scan(&monto)
    if saldo >= monto {
        fmt.Println("Retiro exitoso")
    } else {
        fmt.Println("Saldo insuficiente")
    }
}