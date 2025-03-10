class Persona { String nombre; int edad; }
public class ObjetoNombreEdad {
    public static void main(String[] args) {
        Persona p = new Persona(); p.nombre = "Carlos"; p.edad = 25;
        System.out.println(p.nombre + ", " + p.edad);
    }
}