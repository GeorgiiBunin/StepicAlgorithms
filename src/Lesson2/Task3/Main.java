package Lesson2.Task3;

/**
 * Given two integers n and m, output F(n) mod m
 */

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            long n = sc.nextLong();
            long m = sc.nextLong();
            System.out.println(FibModM(n, m));
        } catch (InputMismatchException e) {
            System.out.println("incorrect input");
        }
    }

    /*
    * This method returns the length of the Pisano period for a divider m
    * */
    private static long GetPisanoPeriod(long m) {
        long a = (long) 0;
        long b = (long) 1;
        long c;
        for (int i = 0; i < m * m; i++) {
            c = (a + b) % m;
            a = b;
            b = c;
            if ((a == 0) && (b == 1)) {
                return i + 1;
            }
        }

        return (long) 0;
    }

    /*
    * this method returns remainder of a huge Fibonacci number (n<=10^7)
    * n is the index of the Fibonacci number
    * */
    private static long FibModM(long n, long m) {
        long r = GetPisanoPeriod(m);

        long first = 0;
        long second = 1;

        long res = r;
        for (int i=1; i<r; i++){
            res = (first+second)%m;
            first = second;
            second = res;
        }
        return res %m;
    }
}