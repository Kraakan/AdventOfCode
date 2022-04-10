package com.company;
import java.util.ArrayList;
import java.io.FileNotFoundException;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        int[] numbers = GetText.Open("day1numbers.txt");
        ArrayList<Integer> numbers1 = new ArrayList<>(numbers.length);
        ArrayList<Integer> numbers2 = new ArrayList<>(numbers.length);

        for (int n:numbers){
            numbers1.add(n);
            numbers2.add(n);
        }
        for (int i=0;i<numbers.length;i++){

            if (numbers[i] == numbers1.get(0)) numbers1.remove(0);

                if (numbers[i] == numbers2.get(0)) numbers2.remove(0);

            for(int j =0;j<numbers1.size();j++){
                if (numbers1.get(j) == numbers2.get(0)) {
                    numbers2.remove(0);
                }
                for(int k=0;k<numbers2.size();k++){
                if(numbers[i]+numbers1.get(j)+numbers2.get(k)==2020){
                    System.out.print("Träff: " + numbers[i]+"+"+ numbers1.get(j) + "+" +  numbers2.get(k) + " = ");
                    System.out.println(numbers[i] + numbers1.get(j) + numbers2.get(k));
                    System.out.print(numbers[i] + "*" + numbers1.get(j) + "*" + numbers2.get(k) + " = ");
                    System.out.println(numbers[i] * numbers1.get(j) * numbers2.get(k));
                    }
                }
            }
        }
    }
}
