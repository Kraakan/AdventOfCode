package com.company;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Passport {
    int byr; // (Birth Year)
    int iyr; // (Issue Year)
    int eyr; // (Expiration Year)
    String hgt; // (Height)
    String hcl; // (Hair Color)
    String ecl; // (Eye Color)
    String pid; // (Passport ID)
    String cid; // (Country ID)

    public Passport(int Byr, int Iyr, int Eyr, String Hgt, String Hcl, String Ecl, String Pid){
        byr = Byr;
        iyr = Iyr;
        eyr = Eyr;
        hgt = Hgt;
        hcl = Hcl;
        ecl = Ecl;
        pid = Pid;
    }
public void setcid(String Cid){
        cid = Cid;
}
public boolean Validate(String param){
        if (param == hgt){
            // a number followed by either cm or in:
            String unit = hgt.substring(hgt.length()-2);
            // If cm, the number must be at least 150 and at most 193.
            if (unit.equals("cm")){
                if(Integer.parseInt(hgt.substring(0,hgt.length()-2))>=150 && Integer.parseInt(hgt.substring(0,hgt.length()-2))<=193) return true;
                else return false;
            }
            // If in, the number must be at least 59 and at most 76.
            else if (unit.equals("in")){
                if(Integer.parseInt(hgt.substring(0,hgt.length()-2))>=59 && Integer.parseInt(hgt.substring(0,hgt.length()-2))<=76) return true;
                else return false;
            }
            else return false;
        }
        else if (param == hcl){
            if (!(hcl.charAt(0) == '#')) return false;
            else if (!(hcl.length()==7)) return false;
            else {
                // exactly six characters 0-9 or a-f
                Pattern hclPattern = Pattern.compile("[0-9[a-f]]", Pattern.CASE_INSENSITIVE);
                if (hclPattern.matcher(hcl.substring(1)).find()) return true;
                else return false;
            }
        }
        else if (param == pid){
                // a nine-digit number, including leading zeroes
            if (pid.length()==9) {
            // Test if number
            Pattern pidPattern = Pattern.compile("[^0-9]", Pattern.CASE_INSENSITIVE);
            if (pidPattern.matcher(pid).find()) return false;
            else return true;
            }
            else return false;
        }
        else return false;
}
public boolean Valid(){
        if (byr<1920||byr>2002){
            return false;
        }
        else if(iyr<2010||iyr>2020){
            return false;
        }
        else if(eyr<2020||eyr>2030){
            return false;
        }
        else if(!Validate(hgt)){
            return false;
        }
        else if(!Validate(hcl)){
            return false;
        }
        else if(!(ecl.equals("amb") || ecl.equals("blu") || ecl.equals("brn") || ecl.equals("gry") || ecl.equals("grn") || ecl.equals("hzl") || ecl.equals("oth") )){
            return false;
        }
        else if(!Validate(pid)){
            return false;
        }
        else return true;
}
}
