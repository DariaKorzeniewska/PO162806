package com.company;
import com.company.Mebel;

import java.time.LocalDate;
import java.util.Calendar;
import java.util.Date;

public class Biurko extends Mebel{
    private LocalDate dataProdukcji;
    private double przekatnaMonitora;

    public Biurko(String nazwa, double dlugosc, double szerokosc, Integer iloscNog, double przekatnaMonitora){
        super(nazwa, dlugosc, szerokosc, iloscNog);
        this.przekatnaMonitora = przekatnaMonitora;
        dataProdukcji = LocalDate.of(Calendar.YEAR, Calendar.MONTH, Calendar.DAY_OF_MONTH);

    }

    public void setDataProdukcji(int rok, int miesiac, int dzien) {
        this.dataProdukcji = LocalDate.of(rok, miesiac, dzien);
    }

    public LocalDate getDataProdukcji() {
        return dataProdukcji;
    }

    @Override
    public String toString(){
        return super.toString() + "\n" + this.getClass().getName() + " [" + getDataProdukcji() + ", " + getDataProdukcji().getDayOfWeek() + ", " + getDataProdukcji().getDayOfYear() + "]";
    }

    @Override
    public boolean equals(Object o){
        return this.equals(o);
    }
}
