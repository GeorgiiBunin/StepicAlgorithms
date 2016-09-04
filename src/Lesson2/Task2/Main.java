package Lesson2.Task2;

import java.util.*;

/**
 * Created by diaq9 on 03-Sep-16.
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            int n = sc.nextInt();
            System.out.println(LastDigitOfFibonacci(n));
        } catch (InputMismatchException e){
            System.out.println("incorrect input");
        }
    }
    /*
    * this method returns last digit of a big Fibonacci number (n<=10^7)
    * n is the index of the Fibonacci number
    * Last of an i-th Fibonacci number F(i) is F(i-1)+F(i-2) mod 10
    * */
    private static int LastDigitOfFibonacci(int n){
        List<Integer> ListOfInteger = new ArrayList<>(n+1);
        ListOfInteger.add(0);
        ListOfInteger.add(1);
        for (int i=2;i<n+1;i++){
            ListOfInteger.add((ListOfInteger.get(i-1)+ListOfInteger.get(i-2))%10);
        }

        return ListOfInteger.get(n);
    }
}
