package main
import "fmt"
func main() {
    var v, r float64
    fmt.Print("Ingrese voltaje y resistencia: ")
    fmt.Scan(&v, &r)
    fmt.Println("Corriente:", v/r)
}