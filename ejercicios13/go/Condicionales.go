package main
import "fmt"
func main() {
    var edad int
    fmt.Print("Ingrese su edad: ")
    fmt.Scan(&edad)
    if edad >= 18 {
        fmt.Println("Mayor de edad")
    } else {
        fmt.Println("Menor de edad")
    }
}