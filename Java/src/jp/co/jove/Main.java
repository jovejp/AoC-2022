package jp.co.jove;

import jp.co.jove.day11.Day11;

public class Main {

    public static void main(String[] args) {
        // day 11
        // sample p2
        System.out.println("p2 sample");
        Day11 day11Sample = new Day11("/day11/day11_1_s.txt");
        day11Sample.process(10000);

        // P2 production
        System.out.println("p2 production");
        Day11 day11 = new Day11("/day11/day11.txt");
        day11.process(10000);
    }
}
