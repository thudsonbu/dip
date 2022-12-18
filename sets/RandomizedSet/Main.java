package sets.RandomizedSet;

public class Main {
  public static void main(String args[]) {
    RandomizedSet set = new RandomizedSet();

    set.insert(0);
    set.remove(0);

    for (int c : set.contents) {
      System.out.println(c);
    }

    set.insert(0);

    for (int c : set.contents) {
      System.out.println(c);
    }

    set.insert(0);

    for (int c : set.contents) {
      System.out.println(c);
    }

    set.insert(1);
    set.insert(2);
    set.insert(3);
    for (int c : set.contents) {
      System.out.println(c);
    }

    set.remove(3);

    for (int c : set.contents) {
      System.out.println(c);
    }
  }
}
