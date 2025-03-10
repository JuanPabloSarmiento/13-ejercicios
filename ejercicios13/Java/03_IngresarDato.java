import java.util.Scanner;
public class IngresarDato {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese un número: ");
        int num = sc.nextInt();
        System.out.println("Número ingresado: " + num);
    }
}