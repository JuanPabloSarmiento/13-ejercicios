import java.util.Scanner;
public class SwitchCalculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("1.Suma 2.Resta: ");
        int op = sc.nextInt();
        System.out.print("Ingrese dos números: ");
        int a = sc.nextInt(), b = sc.nextInt();
        switch(op) { case 1: System.out.println(a + b); break; case 2: System.out.println(a - b); break; }
    }
}