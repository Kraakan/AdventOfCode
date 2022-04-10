package com.company;

import java.io.FileNotFoundException;
import java.util.HashMap;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        String[] text = GetText.Open("input.txt");
        for (int i=0; i<text.length;i++){
            new Bag(text[i]);
        }
        for (String key:Bag.Bags.keySet()
        ) {
            Bag thisbag = Bag.Bags.get(key);
            thisbag.AddContent(thisbag.contentstring);
        }
        System.out.println("finit");
    }
}
