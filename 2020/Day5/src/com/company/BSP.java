package com.company;

import java.util.Comparator;

public class BSP {
    String code;
    int row;
    int column;
    int seatid;
    public BSP(String c){
        code = c;
        Initialise(code);
    }

    void Initialise(String c){
        if (c.length()>6) row = countRow(c);
        if (c.length()>6) column = countColumn(c);
        seatid = 8 * row + column;
    }

    int countRow (String c){
        String RowCode = c.substring(0,7);
        int min = 0;
        int max = 127;
        int returnvalue = -1;
        for (int i=0; i<RowCode.length(); i++){
            if (RowCode.charAt(i)=='F'){
                // Choose lower half
                max = min + (max-min)/2;
                returnvalue = min;
            }
            if (RowCode.charAt(i)=='B'){
                // Choose upper half
                min = min + 1 + (max-min)/2;
                returnvalue = max;
            }
        }

        return returnvalue;
    }

    int countColumn (String c){
        String ColumnCode = c.substring(7);
        int min = 0;
        int max = 7;
        int returnvalue = -1;
        for (int i=0; i<ColumnCode.length(); i++){
            int diff = (max-min)/2;
            if (ColumnCode.charAt(i)=='L'){
                // Choose lower half
                max = min + diff;
                returnvalue = min;
            }
            if (ColumnCode.charAt(i)=='R'){
                // Choose upper half
                min = min + diff +1;
                returnvalue = max;
            }
        }
        return returnvalue;
    }
    public int getId(){
        return seatid;
    }
    public String getCode(){
        return code;
    }

    public static Comparator<BSP> SeatID = new Comparator<BSP>() {

        public int compare(BSP p1, BSP p2) {

            int id1 = p1.getId();
            int id2 = p2.getId();

            if (id1 < id2) return -1;
            if (id1 > id2) return 1;
            return 0;

        }
    };
}
