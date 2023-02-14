package com.company;
import java.time.LocalDate;
import java.util.*;

public class Osoba<T extends Comparable<T>> implements Cloneable, Comparable<Osoba<T>>{
    private String nazwisko;
    private LocalDate dataUrodzenia;

    public Osoba(String nazwisko, LocalDate dataUrodzenia){
        this.nazwisko = nazwisko;
        this.dataUrodzenia = dataUrodzenia;
    }

    @Override
    public String toString(){
        return getClass().getName() + "[ " + this.nazwisko + this.dataUrodzenia.toString() + " ]";
    }

    @Override
    public boolean equals(Object o){
        if(!(o instanceof Osoba)){
            return false;
        }
        Osoba other = (Osoba) o;
        return other.nazwisko.equals(this.nazwisko) && other.dataUrodzenia.isEqual(this.dataUrodzenia);
    }

    @Override
    public int compareTo(Osoba<T> o){
        Osoba other = (Osoba) o;

        if(other.nazwisko.length() > this.nazwisko.length()){
            return -1;
        }
        if(other.nazwisko.length() < this.nazwisko.length()){
            return 1;
        }
        if(other.dataUrodzenia.isAfter(this.dataUrodzenia)){
            return -1;
        }
        if(other.dataUrodzenia.isBefore(this.dataUrodzenia)){
            return 1;
        }
        return 0;
    }
}
