package scopes;

public class Main
{
    // a field so will have scope throughout the class
    static int car = 5;

    public static void main(String[] args)
    {
        // a local variable. It will have scope from the method's opening { to the method's closing }
        int count = 0;

        // we are starting a new block within the method
        // the curly brackets {..} signify a block
        {
        // coffee is a local variable defined only inside this block
            int coffee = 5;
            // we create a variable called car - this is local to this block and successfully hides the field car
            // any work done in this block is done on the local car - the field car is never used
            int car = 15;
            System.out.println(car); // displays 15
            // count is still in scope so let's increment by 1
            System.out.println(count++); // diplays 0 and then increment counts by 1
            System.out.println(++count); // increments count by 1 and then displays it. displays 2
        }

        // note that since the block ended, the integer coffee is no longer defined. So, such as
        // System.out.println(coffee);
        // here would not compile

        // count has remained in scope and visible throughout so it did get incremented
        System.out.println(count); // displays 2

        // we are starting a new block
        {
            // we are creating a variable called coffee. This is completely unrelated to the coffee defined earlier.
            int coffee = 10;
            System.out.println(coffee); // displays 10
        }

        System.out.println(car); // displays 5
    }
}

