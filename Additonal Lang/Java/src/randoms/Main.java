package randoms;

import java.util.Random;

public class Main
{
    public static void main(String args[])
    {
        // create an object called rand which is of class type Random()
        // this object could be named anything but rand is commonly used
        // this object contains a variety of methods to generate random
        // numbers of all types
        Random rand = new Random();

        // display the values for minimum and maximum integer
        // each primitive data type has an associated class type
        // that contains various constants and methods.
        // Use the constants in the Integer class type to find
        // the min and max numbers!
        System.out.println("min int " + Integer.MIN_VALUE);
        System.out.println("max int " + Integer.MAX_VALUE);

        // generate a random integer from min int through max int
        int iresult = rand.nextInt();
        System.out.println(iresult);

        // Pick a number from 0, 1, 2, 3, 4
        // the 5 as the parameter below says to pick from the 5 numbers, starting with 0
        // here we are reusing the variable iresult. It has already been
        // declared so we can just use it.
        iresult = rand.nextInt(5);
        System.out.println(iresult);

        // Now let's pick a number from 5 to 10 by
        // picking from the 6 numbers starting with 0
        // 0, 1, 2, 3, 4, 5
        // now add 5 to that number. So possible choices are
        // 5, 6, 7, 9, 9, 10
        iresult = rand.nextInt(6) + 5;
        System.out.println(iresult);

        // pick a random double between 0.0 and 1.0
        // now we are working with a different data type, double,
        // so we need a new result variable.
        double dresult = rand.nextDouble();
        System.out.println(dresult);
    }
}

