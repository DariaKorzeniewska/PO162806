package com.company;
public class Mebel {
    private String nazwa;
    private double dlugosc;
    private double szerokosc;
    private Integer iloscNog;
    private static int ile;

    public Mebel(String nazwa, double dlugosc, double szerokosc, Integer iloscNog){
        this.nazwa = nazwa;
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
        this.iloscNog = iloscNog;
        ile+=1;

    }

    public Mebel(double dlugosc, double szerokosc, Integer iloscNog){
        this("Jakis Mebel", dlugosc, szerokosc, iloscNog);
    }

    public String getNazwa(){
        return this.nazwa;
    }

    public double getDlugosc() {
        return dlugosc;
    }

    public double getSzerokosc() {
        return szerokosc;
    }

    public Integer getIloscNog(){
        return iloscNog;
    }

    public static int getIle(){
        return ile;
    }

    @Override
    public String toString(){
        if (this.nazwa == "Jakis Mebel"){
            return this.getClass().getName() + " ["  + getDlugosc() + ", " + getSzerokosc() + ", " + getIloscNog() + "]";
        }
        return this.getClass().getName() + " [" + getNazwa() + ", " + getDlugosc() + ", " + getSzerokosc() + ", " + getIloscNog() + "]";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Mebel)) {
            return false;
        }

        Mebel other = (Mebel) o;

        boolean nazwaEquals = (this.nazwa == null && other.nazwa == null) || (this.nazwa != null && this.nazwa.equals(other.nazwa));
        boolean iloscNogEquals = (this.iloscNog == null && other.iloscNog == null) || (this.iloscNog != null && this.iloscNog.equals(other.iloscNog));
        boolean dlugoscEquals = false;
        boolean szerokoscEquals = false;
        if (this.dlugosc == other.dlugosc) {
            dlugoscEquals = true;
        }
        if (this.szerokosc == other.szerokosc) {
            szerokoscEquals = true;
        }

        return nazwaEquals && dlugoscEquals && szerokoscEquals && iloscNogEquals;

    }



}