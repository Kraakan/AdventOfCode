package com.company;

import java.io.FileNotFoundException;

public class Main {

    static int Slope(double right, double down, String[] SlopeArray, boolean draw){
        int xDistance = (int) (right/down * SlopeArray.length);
        int SlopeFactor = (int) Math.ceil (Double.valueOf(xDistance)/Double.valueOf(SlopeArray[0].length()));
        int ouchies = 0;
        for (int i=0; i<SlopeArray.length; i++){
            String Slopeline = "";
            for (int j=0; j<SlopeFactor; j++){
                Slopeline += SlopeArray[i];
            }
            if (draw) System.out.print(Slopeline.substring(0,  (int) (right/down*i)));
            if ((int) (right/down*i) == (right/down*i) && Slopeline.charAt((int) (right/down*i)) == '#'){
                ouchies++;
                if (draw) System.out.print("X");
            }
            else if (draw && (int) (right/down*i) == (right/down*i)) System.out.print("O");
            if (draw) System.out.println(Slopeline.substring( (int) (right/down*i+1)));
        }
        return ouchies;
    }

    public static void main(String[] args) throws FileNotFoundException {
	String[] SlopeArray = GetText.Open("input.txt");

	    int trees1 = Slope(1,1,SlopeArray,false);
        int trees2 = Slope(3,1,SlopeArray,false);
        int trees3 = Slope(5,1,SlopeArray,false);
        int trees4 = Slope(7,1,SlopeArray,false);
        int trees5 = Slope(1,2,SlopeArray,true);

        System.out.print(trees1 + " * " + trees2 + " * " + trees3 + " * " + trees4 + " * " + trees5 + " = ");
        double product = Double.valueOf(trees1)*Double.valueOf(trees2)*Double.valueOf(trees3)*Double.valueOf(trees4)*Double.valueOf(trees5);
        System.out.println(product);
    }
}
