package com.company;

import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        int byr; // (Birth Year)
        int iyr; // (Issue Year)
        int eyr; // (Expiration Year)
        String hgt; // (Height)
        String hcl; // (Hair Color)
        String ecl; // (Eye Color)
        String pid; // (Passport ID)
        String cid; // (Country ID)
        String filetext = GetText.Open("input.txt");
        //System.out.println(filetest);

        String [] textArray = filetext.split("\r\n \r");
        String [] tempArray;

        ArrayList<Passport> ValidPassports = new ArrayList<>();
        for (int i =0; i<textArray.length;i++){
            byr = -1;
            iyr = -1;
            eyr = -1;
            hgt = null;
            hcl = null;
            ecl = null;
            pid = null;
            cid = null;
            tempArray = textArray[i].split(" ");
            for (int j=0; j<tempArray.length;j++){
                String reading = tempArray[j].replace("\n", "").replace("\r","");
                if(reading.length()>4){
                switch (reading.substring(0,3)){
                    case "byr":
                        byr = Integer.parseInt(reading.substring(4));
                        break;

                    case "iyr":
                        iyr = Integer.parseInt(reading.substring(4));
                        break;

                    case "eyr":
                        eyr = Integer.parseInt(reading.substring(4));
                        break;

                    case "hgt":
                        hgt = reading.substring(4);
                        break;

                    case "hcl":
                        hcl = reading.substring(4);
                        break;

                    case "ecl":
                        ecl = reading.substring(4);
                        break;

                    case "pid":
                        pid = reading.substring(4);
                        break;

                    case "cid":
                        cid = reading.substring(4);
                        break;
                    default:
                        System.out.println("Error!");
                }
                }
            }
            if (byr != -1 &&
            iyr != -1 &&
            eyr != -1 &&
            hgt != null &&
            hcl != null &&
            ecl != null &&
            pid != null){
                Passport p = new Passport(byr, iyr, eyr, hgt, hcl, ecl, pid);
                if (cid != null) p.setcid(cid);
                if (p.Valid()) ValidPassports.add(p);
            }
        }
        System.out.println(ValidPassports.size());
    }
}
