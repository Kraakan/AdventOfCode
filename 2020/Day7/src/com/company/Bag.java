package com.company;

import java.util.ArrayList;
import java.util.HashMap;

public class Bag {
    String name;
    String contentstring;
    public static HashMap<String,Bag> Bags = new HashMap();
    ArrayList<Bag> contains = new ArrayList();

    public String GetName(){
        return name;
    }

    public Bag(String s){
        String[] split = s.split("s contain");
        name = split[0];
        contentstring = split[1].trim();
        Bags.put(name, this);
    }

    public void AddContent(String c){
        int bagnr;
        Bag bagtype;
        String[] contentarray = c.split(",");
        for (int i=0; i<contentarray.length; i++){
            bagnr = contentarray[i].charAt(1);
            bagtype = Bag.Bags.get(contentarray[i].substring(2).trim());
            for (int j=0; j<bagnr;j++){
                contains.add(bagtype);
            }
        }
    }

    // Överflödig metod
    public static Bag Lookup(String s){
        Bag returnbag = null;
        for (String key:Bags.keySet()
             ) {
            if (Bags.get(s).GetName() == s){
                returnbag = Bags.get(s);
            }
        }
        if (returnbag == null) returnbag = new Bag(s);
        return returnbag;
    }

}
