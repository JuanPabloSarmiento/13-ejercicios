package main
import "fmt"
func main() {
    var nombre string
    fmt.Print("Ingrese su nombre: ")
    fmt.Scan(&nombre)
    fmt.Println("Hola,", nombre)
}