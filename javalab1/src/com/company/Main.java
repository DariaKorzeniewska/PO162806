package com.company;
import java.util.Scanner;

public class Main {

    public static void a(){
        Scanner objekt = new Scanner(System.in);
        System.out.println("Podaj n: ");
        Integer n = objekt.nextInt();
        System.out.println("Podaj tyle liczb: ");
        float suma = 0;
        for (int i = 1; i <= n; i++){
            Float liczba = objekt.nextFloat();
            suma+=liczba;
        }
        System.out.println(suma);
    }

    public static void b(){
        Scanner objekt = new Scanner(System.in);
        System.out.println("Podaj n: ");
        Integer n = objekt.nextInt();
        System.out.println("Podaj tyle liczb: ");
        float iloczyn = 0;
        for (int i = 1; i <= n; i++){
            Float liczba = objekt.nextFloat();
            iloczyn*=liczba;
        }
        System.out.println(iloczyn);
    }

    public static void c(){
        Scanner objekt = new Scanner(System.in);
        System.out.println("Podaj n: ");
        Integer n = objekt.nextInt();
        System.out.println("Podaj tyle liczb: ");
        float suma = 0;
        for (int i = 1; i <= n; i++){
            Float liczba = objekt.nextFloat();
            if (liczba < 0){
                liczba *= -1;
            }
            suma+=liczba;
        }
        System.out.println(suma);
    }

    public static void d(){
        Scanner objekt = new Scanner(System.in);
        System.out.println("Podaj n: ");
        Integer n = objekt.nextInt();
        System.out.println("Podaj tyle liczb: ");
        float suma = 0;
        for (int i = 1; i <= n; i++){
            Float liczba = objekt.nextFloat();
            if(liczba < 0){
                liczba *= -1;
            }
            suma+=Math.sqrt(liczba);
        }
        System.out.println(suma);
    }

    public static void e(){
        Scanner objekt = new Scanner(System.in);
        System.out.println("Podaj n: ");
        Integer n = objekt.nextInt();
        System.out.println("Podaj tyle liczb: ");
        float iloczyn = 1;
        for (int i = 1; i <= n; i++){
            Float liczba = objekt.nextFloat();
            if (liczba < 0){
                liczba *= -1;
            }
            iloczyn*=liczba;
        }
        System.out.println(iloczyn);
    }

    public static void f(){
        Scanner objekt = new Scanner(System.in);
        System.out.println("Podaj n: ");
        Integer n = objekt.nextInt();
        System.out.println("Podaj tyle liczb: ");
        float suma = 0;
        for (int i = 1; i <= n; i++){
            Float liczba = objekt.nextFloat();
            suma+=Math.pow(liczba,2);
        }
        System.out.println(suma);
    }


    public static void main(String[] args) {
        System.out.print("zadanie1: ");
        a();


    }
}
