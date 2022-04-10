package com.company;

import java.io.FileNotFoundException;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        String text = GetText.Open("input.txt");
        // System.out.println(text);
        String[] groups = text.split("\r\n\r\n");
        int [] counts = new int[groups.length];
        int sum =0;


        for (int i=0; i<groups.length; i++){
            String group[] = groups[i].split("\r\n");
            String chars = group[0];
            String newchars = "";
            int count = 0;

            for (int j=0; j<chars.length(); j++){
                int charsfound = 0;
                for (int k=0; k<group.length; k++){
                    for (int l=0; l<group[k].length();l++){
                        if (group[k].charAt(l)==chars.charAt(j)){
                            charsfound++;
                            l=group[k].length();
                        }
                    }

                }
                if (charsfound==group.length) newchars += chars.charAt(j);
            }
            chars = newchars;
            for (int k=0; k<chars.length(); k++){
                count++;
            }
            counts[i] = count;
        }
        for (int i=0; i<counts.length;i++){
            sum+=counts[i];
        }
        System.out.println(sum);
    }
}
