package main
import (
    "fmt"
    "math/rand"
    "time"
)
func main() {
    equipos := []string{"Argentina", "Francia", "Brasil", "Inglaterra"}
    rand.Seed(time.Now().UnixNano())
    fmt.Println(equipos[rand.Intn(len(equipos))], "vs", equipos[rand.Intn(len(equipos))])
}