package com.company;

import java.sql.SQLOutput;

public class Main {

    public static void main(String[] args) {
        int[] tab = {1, 2, 3, 4, 5};
        int[] tab_copy = new int[tab.length];
        System.arraycopy(tab, 0, tab_copy, 0, tab.length);
        wypisz(tab_copy);

    }

    public static void wypisz(int[] tablica){
        System.out.print("[ ");
        for(int i = 0; i < tablica.length; i++){
            System.out.print(tablica[i] + ", ");
        }
        System.out.print("]");
    }
}
