package com.company;
import com.company.Osoba;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) {
	// TEST OSOBA
        Osoba o1 = new Osoba("Kowalski", LocalDate.of(2000,12,12));
        Osoba o2 = new Osoba("Kowalski", LocalDate.of(2004,2,14));
        Osoba o3 = new Osoba("Szymanko", LocalDate.of(1996,5,30));
        Osoba o4 = new Osoba("Kozlowski", LocalDate.of(1996,5,30));
        Osoba o5 = new Osoba("Korzeniewska", LocalDate.of(2000, 6, 1));

        ArrayList grupa = new ArrayList();
        grupa.add(o1);
        grupa.add(o2);
        grupa.add(o3);
        grupa.add(o4);
        grupa.add(o5);

        for(Object i : grupa){
            System.out.println(i);
        }
        Collections.sort(grupa);
        System.out.println("\n");
        for(Object i : grupa){
            System.out.println(i);
        }
        

    }
}
