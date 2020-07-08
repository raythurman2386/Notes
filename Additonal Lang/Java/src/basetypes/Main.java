package basetypes;

public class Main {
  public static void main(String args[]) {
    // Create some numbers to work with
    int a = 2;
    int b = 3;
    double ba = 11.5;

    /*
    Manipulate those numbers and output results
    arithmetic includes + - / *
    the result on a double and an int results in a double
    */
    double result = ba / a;
    System.out.println(result);

    // Arithmetic of an integer and an integer is an int
    System.out.println(a + b);

    // int divided by an int is an int
    System.out.println(b / a);

    // The modulus % returns the remainder of the division
    // normally used on positive integers
    System.out.println(b % a);

    // Strings
    String strA = "North ";
    String strB = "Harrison";

    String strCombined = strA + strB;
    System.out.println(strCombined);

    // Java aalso handles compound and increment operators
    a += b; // Same as a = a + b
    System.out.println(a);

    b++; // same as b = b + 1
    System.out.println(b);
  }
}