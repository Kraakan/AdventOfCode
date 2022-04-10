package com.company;

public class Password {
    private int min;
    private int max;
    private char letter;
    private String password;

    public Password (int m, int M,char l, String psw){
        min = m;
        max = M;
        letter = l;
        password = psw;
    }
public void SetLetter(char a){

}
public void SetMin(int n){

}
public void SetMax(int n){

}
public void SetPassword(String psw){

}
public int getMin(){return min;}

public int getMax(){return max;}

public char getLetter(){return letter;}

public String getPassword(){return password;}

public boolean Validate(){
    int lettercount = 0;

        if ((password.charAt(min-1) == letter && password.charAt(max-1) != letter) || (password.charAt(min-1) != letter && password.charAt(max-1) == letter)) return true;
        else return false;
}
}
