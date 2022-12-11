package jp.co.jove.day11;


import jp.co.jove.FileUtils;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;

public class Day11 {
    ArrayList<Monkey> monkeyList = new ArrayList<>();
    BigInteger commonModData = new BigInteger("1");
    String filePath;

    public Day11(String filePath) {
        this.filePath = filePath;
    }

    private void loadMonkey() {
        String tmpFilePath = this.getClass().getResource(this.filePath).getPath();
        ArrayList<ArrayList> sampleDataList = FileUtils.readFileStep(tmpFilePath, 6);
        // add monkey
        for (int i = 0; i < sampleDataList.size(); i++) {
            this.monkeyList.add(this.makeMonkey(sampleDataList.get(i)));
        }
    }

    private Monkey makeMonkey(ArrayList<String> stepList) {
        Monkey monkey = new Monkey();
        String tmpStrLine;
        String[] tmpList;
        ArrayList<BigInteger> tmpDataList = new ArrayList<>();

        for (String s : stepList) {
            tmpStrLine = s;
            if (tmpStrLine.trim().startsWith("Monkey")) {
                tmpList = tmpStrLine.split(" ");
                monkey.monkeyIndex = Integer.parseInt(tmpList[1].substring(0, tmpList[1].length() - 1).strip());
            } else if (tmpStrLine.trim().startsWith("Starting items:")) {
                tmpList = tmpStrLine.replace("Starting items:", "").trim().split(",");
                for (String value : tmpList) {
                    tmpDataList.add(new BigInteger(value.trim()));
                }
                monkey.dataList = tmpDataList;
            } else if (tmpStrLine.trim().startsWith("Operation:")) {
                tmpList = tmpStrLine.replace("Operation:", "").trim().split(" ");
                monkey.operation = tmpList[3].trim();
                if (tmpList[4].trim().equals("old")) {
                    monkey.operationValue = 0;
                } else {
                    monkey.operationValue = Integer.parseInt(tmpList[4].trim());
                }
            } else if (tmpStrLine.trim().startsWith("Test:")) {
                monkey.testDivNum = Integer.parseInt(tmpStrLine.replace("Test: divisible by", "").trim());
                this.commonModData = this.commonModData.multiply(BigInteger.valueOf(monkey.testDivNum));
            } else if (tmpStrLine.trim().startsWith("If true:")) {
                monkey.trueMonkey = Integer.parseInt(tmpStrLine.replace("If true: throw to monkey", "").trim());
            } else if (tmpStrLine.trim().startsWith("If false:")) {
                monkey.falseMonday = Integer.parseInt(tmpStrLine.replace("If false: throw to monkey", "").trim());
            }
        }
        return monkey;
    }

    private BigInteger computerRiskValue(String operation, BigInteger firstData, BigInteger secondData) {
        switch (operation) {
            case "+":
                return firstData.add(secondData);
            case "-":
                return firstData.subtract(secondData);
            case "*":
                return firstData.multiply(secondData);
            default:
                System.err.println("operation error!!!");
                return new BigInteger("0");
        }
    }

    private void processThrow() {
        Monkey tmpMonkey;
        BigInteger secondValue;
        BigInteger oldData;
        BigInteger newRiskValue;
        for (Monkey monkey : this.monkeyList) {
            tmpMonkey = monkey;
            for (int j = 0; j < tmpMonkey.dataList.size(); j++) {
                oldData = tmpMonkey.dataList.get(j);
                tmpMonkey.throwTimes += 1;
                if (tmpMonkey.operationValue == 0) {
                    secondValue = oldData;
                } else {
                    secondValue = BigInteger.valueOf(tmpMonkey.operationValue);
                }
                newRiskValue = computerRiskValue(tmpMonkey.operation, oldData, secondValue).mod(this.commonModData);
                if (newRiskValue.mod(BigInteger.valueOf(tmpMonkey.testDivNum)).intValue() == 0) {
                    this.monkeyList.get(tmpMonkey.trueMonkey).dataList.add(newRiskValue);
                } else {
                    this.monkeyList.get(tmpMonkey.falseMonday).dataList.add(newRiskValue);
                }
            }
            this.monkeyList.get(tmpMonkey.monkeyIndex).dataList.clear();
        }
    }

    private void printResult() {
        ArrayList<BigInteger> timeList;
        timeList = new ArrayList<>();
        for (Monkey monkey : this.monkeyList) {
            timeList.add(BigInteger.valueOf(monkey.throwTimes));
        }
        Collections.sort(timeList, Collections.reverseOrder());
        System.out.println(timeList.get(0).multiply(timeList.get(1)));
    }

    public void process(int times) {
        this.loadMonkey();
        for (int i = 0; i < times; i++) {
            this.processThrow();
        }
        this.printResult();
    }
}
