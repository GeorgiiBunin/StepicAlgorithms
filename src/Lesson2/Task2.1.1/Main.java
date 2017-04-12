package Lesson2.Task1;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by diaq9 on 03-Sep-16.
 */

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(FibLessthan40(n));
        // put your code here
    }
    private static int FibLessthan40 (int n){
        ArrayList<Integer> array = new ArrayList<>(40);
        array.add(0);
        array.add(1);
        //int res = 0;
        for (int i = 2; i<=n; i++){
            array.add(array.get(i-1)+array.get(i-2));
        }
        return array.get(n);
    }
}
