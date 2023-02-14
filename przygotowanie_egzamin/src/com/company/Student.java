package com.company;
import com.company.Osoba;

import java.time.LocalDate;

public class Student<T extends Comparable<T>> extends Osoba implements Cloneable, Comparable<Student<T>>{
    private double sredniaOcen;

    public Student(String nazwisko, LocalDate dataUrodzenia, double sredniaOcen){
        super(nazwisko,dataUrodzenia);
        this.sredniaOcen = sredniaOcen;
    }

    @Override
    public int compareTo(Student<T> s){
        Student other = (Student) s;

        if(other.compareTo(this) == 0){
            if(other.sredniaOcen > this.sredniaOcen){
                return -1;
            }
            if(other.sredniaOcen < this.sredniaOcen){
                return 1;
            }
            return 0;
        }
        return other.compareTo(this);
    }

}
