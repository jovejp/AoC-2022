package jp.co.jove;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class FileUtils {
    public static ArrayList readFileStep(String filePath, int stepLines) {
        BufferedReader reader;
        ArrayList dataList = new ArrayList<String>();
        ArrayList subDataList = new ArrayList<String>();
        try {
            reader = new BufferedReader(new FileReader(filePath));
            String line = reader.readLine();
            int countIndex = 0;
            while (line != null) {

                subDataList.add(line);
                countIndex += 1;

                if (countIndex == stepLines) {
                    dataList.add(subDataList);
                    subDataList = new ArrayList<String>();
                    countIndex = 0;
                }
                // read next line
                line = reader.readLine();
                if (line.trim().isBlank()) {
                    line = reader.readLine();
                }
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            return dataList;
        }
    }
}
