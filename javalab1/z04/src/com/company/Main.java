package com.company;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        System.out.println("a) " + countChar("kajak", 'k'));
        System.out.println("b) " + countSubStr("lubaalub", "lub"));
        System.out.println(countSubStr("DX", "XD"));
        System.out.println("c) " + middle("middle"));
        System.out.println(middle("kot"));
        System.out.println("d) " + repeat("kot", 3));
    }

    public static int countChar(String str, char c){
        int n = str.length();
        int counter = 0;
        for (int i=0; i<n; i++){
            if (str.charAt(i) == c){
                counter+=1;
            }
        }
        return counter;
    }

    public static int countSubStr(String str, String subStr){
        int counter = 0;
        int subCounter = 0;
        int fakeI = 0;
        int n = str.length();
        int m = subStr.length();
        if (n < m) return 0;
        for (int i=0; i<n; i++){
            fakeI = i;
            counter = 0;
            for (int j=0; j<m; j++){
                if (str.charAt(fakeI) == subStr.charAt(j)) {
                    counter += 1;
                    fakeI += 1;
                }
                if (fakeI >= n){
                    j=m-1;
                    counter=0;
                }

                if (counter == m){
                    subCounter+=1;
                }
            }}
        return subCounter;
    }

    public static String middle(String str){
        int len = str.length();
        if (len%2 == 0){
            String s = "" + str.charAt(len/2);
            s += str.charAt((len/2)-1);
            return s;
        }

        String s = "" + str.charAt(len/2);
        return s;

    }

    public static String repeat(String str, int n){
        String napis = "";
        for (int i=0; i<n; i++){
            napis += str;
        }
        return napis;
    }
    //where




}
