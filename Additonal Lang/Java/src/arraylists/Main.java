package arraylist;

import java.util.ArrayList;   // the ArrayList requires this import
import java.util.Collections; // required import for sorting the ArrayList
import java.util.Comparator;  // required import for sorting the ArrayList in descending order
import java.util.List;        // the List requires this import

public class Main {
  public static void main(String[] args) {
    List<String> cities = new ArrayList<>();

    // add a new String to the ArrayList. ArrayList maintains order,
    // so Lehi is at index 0, Seattle at index 1, San Francisco at index 2, and so on
    cities.add("Corydon");
    cities.add("Ramsey");
    cities.add("Clarksville");
    cities.add("Jeffersonville");
    cities.add("New Albany");
    // Add item after a specific index
    cities.add(3, "Louisville");

    System.out.println("\n*** The ArrayList ***");
    System.out.println(cities);
    System.out.println("The element at index 0 is " + cities.get(0));

    System.out.println("\n*** Contains ***");
    System.out.println("The ArrayList contains \"Corydon\": " + cities.contains("Corydon"));
    System.out.println("The ArrayList contains \"New York\": " + cities.contains("New York"));

    System.out.println("\n*** Replacing index 3 ***");
    System.out.println("The Original index 3: " + cities.get(3));
    cities.set(3, "Portland");
    System.out.println("The new index 3: " + cities.get(3));

    // Remove a specific index
    cities.remove(3);

    // Loop through the elements in the List
    System.out.println("\n*** Looping through ArrayList ***");
    for (String c : cities) {
      System.out.println(c);
    }

    for (int i = 0; i < cities.size(); i++) {
      System.out.println("Index: " + i + " Value: " + cities.get(i));
    }

    System.out.println("\nSort in Alphabetical Order");
    // Use the Collections.sort(ArrayList) method to sort the ArrayList in ascending order. This actually changes the order of the ArrayList.
    Collections.sort(cities);
    for (int i = 0; i < cities.size(); i++)
    {
        System.out.println("Index: " + i + " Value: " + cities.get(i));
    }

    System.out.println("\nSort in Reverse Alphabetical Order");
    // To sort in descending order, Use the Collections.sort(ArrayList,  Comparator.reverseOrder()) method
    // This actually changes the order of the ArrayList.
    Collections.sort(cities, Comparator.reverseOrder());
    for (int i = 0; i < cities.size(); i++)
    {
        System.out.println("Index: " + i + " Value: " + cities.get(i));
    }

    // To clear the ArrayList use clear()
    // Java would automatically free up the memory allotted to the ArrayList when the ArrayList goes out of scope,
    // so at the end of this method.
    System.out.println("\nThe empty ArrayList");
    cities.clear();
    System.out.println(cities);
  }
}