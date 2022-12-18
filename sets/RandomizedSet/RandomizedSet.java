package sets.RandomizedSet;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.Random;

public class RandomizedSet {
  ArrayList<Integer> contents;
  HashMap<Integer, Integer> map;
  Random rand;

  public RandomizedSet() {
    this.contents = new ArrayList<>();
    this.map = new HashMap<>();
    this.rand = new Random();
  }

  public boolean insert(int val) {
    if (this.map.containsKey(val)) {
      return false;
    }

    contents.add(val);
    this.map.put(val, contents.size() - 1);

    return true;
  }

  public boolean remove(int val) {
    if (!this.map.containsKey(val)) {
      return false;
    }

    int contentsIdx = this.map.get(val);
    this.contents.remove(contentsIdx);
    this.map.remove(val);

    if (this.contents.size() > 0) {
      int replacement = this.contents.remove(contents.size() - 1);

      if (contentsIdx < this.contents.size()) {
        this.contents.add(contentsIdx, replacement);
        this.map.put(replacement, contentsIdx);
      } else {
        this.contents.add(replacement);
        this.map.put(replacement, this.contents.size() - 1);
      }
    }

    return true;
  }

  public int getRandom() {
    int location = this.rand.nextInt(this.contents.size());

    return this.contents.get(location);
  }
}
