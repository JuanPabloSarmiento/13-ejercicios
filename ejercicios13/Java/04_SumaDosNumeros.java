import java.util.Scanner;
public class SumaDosNumeros {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese dos números: ");
        int a = sc.nextInt(), b = sc.nextInt();
        System.out.println("Suma: " + (a + b));
    }
}