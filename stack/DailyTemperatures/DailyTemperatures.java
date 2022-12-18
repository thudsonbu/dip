package DailyTemperatures;

import java.util.Stack;

// Given an array of integers temperatures represents the daily temperatures,
// return an array answer such that answer[i] is the number of days you have to
// wait after the ith day to get a warmer temperature. If there is no future
// day for which this is possible, keep answer[i] == 0 instead.

public class DailyTemperatures {
  public int[] dailyTemperatures(int[] temperatures) {
    // Create a stack that will store the indexes for days that haven't seen a
    // temperature higher.
    Stack<Integer> stack = new Stack<>();
    int[] answer = new int[temperatures.length];

    stack.push(0);

    for (int i = 1; i < temperatures.length; i++) {
      int dailyTemp = temperatures[i];

      // Remove items from the stack if the temperature is higher and add the
      // distance from the item's index to the current index to the answers
      // array.
      while (stack.size() > 0 && temperatures[stack.peek()] < dailyTemp) {
        int idx = stack.pop();

        answer[idx] = i - idx;
      }

      stack.push(i);
    }

    return answer;
  }
}
