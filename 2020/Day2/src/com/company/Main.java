package com.company;
import java.io.FileNotFoundException;
import java.util.ArrayList;

import static java.lang.Integer.parseInt;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        String text = GetText.Open("input.txt");

        ArrayList<Password> PswList = new ArrayList<>();

        String[] textArray = text.split("\n");
        String[] pswContent;

        for (int i =0; i<textArray.length; i++){
            pswContent = textArray[i].split(" ");
            String[] nums = pswContent[0].split("-");
            int min = parseInt(nums[0]);
            int max = parseInt(nums[1]);

            char ltr = pswContent[1].charAt(0);

            String psw = pswContent[2];

            PswList.add(new Password(min, max, ltr, psw));
        }

        int validCount = 0;
        for (int i = 0; i<PswList.size(); i++){
            if (PswList.get(i).Validate()) validCount ++;
        }
        System.out.println(PswList.size());
        System.out.println(validCount);
    }
}
