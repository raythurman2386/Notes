package castings;

public class Main
{
    public static void main(String args[])
    {
        int myInt = 9;
        // Widening casting happens automatically.
        // An integer is automatically casted, converted, to a double
        double myDouble = myInt;

        // String conversion happens automatically allowing us
        // to print values of integers, doubles, among others
        System.out.println("myInt = " + myInt);
        System.out.println("myDouble = " + myDouble);

        // this just displays a blank line
        System.out.println();

        double my2double = 9.78;
        // Narrowing casting must be done manually
        // notice the addition of (int) in this expression
        // that says to manually convert the double after it
        // to an int.
        int my2int = (int) my2double;

        System.out.println("my2double = " + my2double);
        System.out.println("my2int = " + my2int);
    }
}

