package ValidParens;

import java.util.Stack;

public class Main {
  public static void main(String args[]) {
    System.out.println(Main.isValid("()")); // true
    System.out.println(Main.isValid("()[]{}")); // true
    System.out.println(Main.isValid("(]")); // false
    System.out.println(Main.isValid("([)]")); // false
    System.out.println(Main.isValid("{[]}")); // true
  }

  public static boolean isValid(String s) {
    if (s.length() == 0) {
      return true;
    }

    Stack<String> stack = new Stack<String>();

    for (int i = 0; i < s.length(); i++) {
      String ch = s.substring(i, i + 1);

      try {
        String nextClose = Main.getNextClose(ch);

        stack.push(nextClose);
      } catch (Error e) {
        if (stack.size() == 0) {
          return false;
        }

        String cl = stack.pop();

        if (!ch.equals(cl)) {
          return false;
        }
      }
    }

    if (stack.size() > 0) {
      return false;
    }

    return true;
  }

  public static String getNextClose(String ch) {
    if (ch.equals("(")) {
      return ")";
    } else if (ch.equals("[")) {
      return "]";
    } else if (ch.equals("{")) {
      return "}";
    }

    throw new Error("Not an opening");
  }
}
