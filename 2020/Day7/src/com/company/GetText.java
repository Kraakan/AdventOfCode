package com.company;

import java.io.*;

public class GetText {
    public static String[] Open(String filename) throws FileNotFoundException {
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
            return text.toString().split("\r\n");
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
