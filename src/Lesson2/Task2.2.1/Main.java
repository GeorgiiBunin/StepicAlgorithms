import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.println(GCD(a,b));
    }
    private static int GCD (int a, int b){
        assert a>=0; assert b>=0;
        if (a == 0) return b;
        if (b == 0) return a;
        if (a>=b) return GCD(a%b,b);
        if (b>=a) return GCD(a,b%a);
        return 1;
    }
}