package com.company;
import com.company.Mebel;
import com.company.Biurko;

import java.lang.reflect.Array;

public class Main {
    public static void main(String[] args) {
        Mebel maly = new Mebel("Maly Mebel", 1, 0.5, 4);
        System.out.println(maly);
        System.out.println(Mebel.getIle());
        Mebel sredni = new Mebel(2,1,4);
        System.out.println(sredni);
        Biurko maleBiurko = new Biurko("Male Biurko", 2, 1, 4, 22);
        maleBiurko.setDataProdukcji(2005, 2, 28);
        System.out.println(maleBiurko);
        System.out.println(Mebel.getIle());
        Mebel[][] spis;
        spis = new Mebel[2][2];
        spis[0][0] = sredni;
        spis[0][1] = maly;
        spis[1][0] = maleBiurko;
        spis[1][1] = sredni;

        for (int i=0; i<2; i++){
            for (int j=0; j<2; j++){
                System.out.println(spis[j][i]);
            }
        }

        String[][] spisNazw;
        spisNazw = new String[2][2];
        spisNazw[0][0] = sredni.getNazwa();
        spisNazw[0][1] = maly.getNazwa();
        spisNazw[1][0] = maleBiurko.getNazwa();
        spisNazw[1][1] = sredni.getNazwa();
        System.out.println("\n\n");

        for (Mebel[] i: spis) {
            for (Mebel j: i){
                System.out.println(j);
            }
        }

        System.out.println(sredni.equals(maly));
        System.out.println(sredni.equals(maleBiurko));

        int licz=0;
        String klasySpis = "";
        for (int i=0; i<2; i++){
            for (int j=0; j<2; j++){
                if (spis[j][i] instanceof Biurko){
                    licz+=1;
                }
                klasySpis += spis[j][i].getClass().getName();
                klasySpis += ", ";
                }
            }
        System.out.println(licz);

        System.out.println(klasySpis);


    }
}