package maps.UniqueOccurrences;

import java.util.HashMap;
import java.util.HashSet;

public class UniqueOccurrences {
  public static boolean uniqueOccurrences(int[] arr) {
    // Iterate through the array of items recording the number of occurrences
    // in a hashmap from value to count of occurrences.
    HashMap<Integer,Integer> countMap = new HashMap<>();

    for (int item : arr) {
      if (countMap.containsKey(item)) {
        int currentCount = countMap.get(item);
        countMap.replace(item, currentCount + 1);
      } else {
        countMap.put(item, 1);
      }
    }

    // Iterate through key value pairs of hashmap adding to a set. If the set
    // already contains a specific count of occurrences return false.
    HashSet<Integer> occurSet = new HashSet<Integer>();

    for (HashMap.Entry<Integer, Integer> entry : countMap.entrySet()) {
      Integer value = entry.getValue();

      if (occurSet.contains(value)) {
        return false;
      }

      occurSet.add(value);
    }

    return true;
  }
}
