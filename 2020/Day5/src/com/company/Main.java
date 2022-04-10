package com.company;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        String[] text =GetText.Open("input.txt").split("\n");

        ArrayList<BSP> BSPList = new ArrayList();

        for (int i=0;i<text.length;i++){
            if (text[i].length()>6) BSPList.add(new BSP(text[i].trim()));
        }
        Collections.sort(BSPList, BSP.SeatID);

        // for (int i=28; i<842;i++)
        for (int i=1; i<BSPList.size()-1;i++){
                if (!(BSPList.get(i+1).getId() == BSPList.get(i).getId() +1)) System.out.println(BSPList.get(i).getId()+1);
        }
    }
}
