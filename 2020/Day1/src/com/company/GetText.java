package com.company;

import java.io.*;

public class GetText {
    public static int[] Open(String filename) throws FileNotFoundException {
        try {
            String line = null;
            InputStreamReader data = new InputStreamReader(new FileInputStream(filename), "Windows-1252");
            BufferedReader getText = new BufferedReader(data);
            // System.out.println("DEBUG - Encoding:" + data.getEncoding());
            StringBuilder text = new StringBuilder();
            String ls = System.getProperty("line.separator");
            while(null != (line = getText.readLine())) {
                text.append(line);
                text.append(ls);
            }
            getText.close();


            String [] txtArray = text.toString().split(ls);
            int [] numArray = new int[txtArray.length];
            for (int i=0; i<txtArray.length;i++){
                try {
                    numArray[i] = Integer.parseInt(txtArray[i]);
                }
                catch (NumberFormatException e)
                {
                    System.out.println("Error: not int!");
                }
            }
            return numArray;
        }
        catch (FileNotFoundException e)
        {
            System.out.println("Kunde inte hitta filen '" + filename + "'");
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println("IOException!");
            e.printStackTrace();
        }

        return null;
    }
}
