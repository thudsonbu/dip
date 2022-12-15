package permutations.GenerateParenthesis;

import java.util.ArrayList;
import java.util.List;

public class Main {
  public static void main(String args[]) {
    System.out.println(Main.generateParenthesis(3));
  }

  public static List<String> generateParenthesis(int n) {
    List<String> result = new ArrayList<String>();

    Main.generateParenthesis(n, n, "", result);

    return result;
  }

  public static void generateParenthesis(int open, int close, String s, List<String> result) {
    if (open == 0 && close == 0) {
      result.add(s);
    }

    if (open > 0) {
      Main.generateParenthesis(open - 1, close, s + "(", result);
    }

    if (close > open) {
      Main.generateParenthesis(open, close - 1, s + ")", result);
    }
  }
}
