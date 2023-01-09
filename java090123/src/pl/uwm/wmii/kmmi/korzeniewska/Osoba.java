package pl.uwm.wmii.kmmi.korzeniewska;
import java.io.*;
import java.util.*;

import java.time.LocalDate;

public class Osoba implements Comparable<Osoba>{
    private String nazwisko;
    private LocalDate dataUrodzenia;

    public Osoba(String nazwisko, LocalDate dataUrodzenia){
        this.nazwisko = nazwisko;
        this.dataUrodzenia = dataUrodzenia;
    }

    public int compareTo(Osoba o){
        if (this.nazwisko == o.nazwisko){
            if (this.dataUrodzenia.isBefore(o.dataUrodzenia)){
                return 1;
            }
            if (this.dataUrodzenia.isAfter(o.dataUrodzenia)){
                return -1;
            }
            return 0;
        }
        if (this.dataUrodzenia.isBefore(o.dataUrodzenia)){
            return 1;
        }
        if (this.dataUrodzenia.isAfter(o.dataUrodzenia)){
            return -1;
        }
        return 0;
    }

    @Override
    public String toString(){
        return "Klasa:  " + this.getClass().getName() + "  [" + this.nazwisko + "]  " + this.dataUrodzenia;
    }

    @Override
    public boolean equals(Object other){
        Osoba o = (Osoba) other;
        return o.nazwisko == this.nazwisko && o.dataUrodzenia == this.dataUrodzenia;
    }
}

