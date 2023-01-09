package com.company;
import pl.uwm.wmii.kmmi.korzeniewska.Osoba;
import java.time.LocalDate;
import java.util.Arrays;


//zad2
public class Main {

    public static void main(String[] args) {
	    Osoba o1 = new Osoba("Kowalski", LocalDate.of(2023,1,8) );
        System.out.println(o1);
        Osoba o2 = new Osoba("Rennewicz", LocalDate.of(2000, 12, 1));
        System.out.println(o1==o2);
        Osoba o3 = new Osoba("Kowalski", LocalDate.of(2000, 12, 1));
        Osoba o4 = new Osoba("Nawicki", LocalDate.of(1999, 3, 12));
        Osoba o5 = new Osoba("Jankowski", LocalDate.of(1890, 3, 18));

        Osoba[] grupa = {o1, o2, o3, o4, o5};
        for (int i=0; i<5; i++){
            System.out.println(grupa[i]);
        }
        System.out.println("");
        Arrays.sort(grupa);
        for (int i=0; i<5; i++) {
            System.out.println(grupa[i]);
        }


    }
}


