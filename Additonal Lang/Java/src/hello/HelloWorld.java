package hello;
// Java is an object oriented language
// Most projects will revolve around classes
public class HelloWorld {
  // All classes will need a main method
  public static void main(String[] args) {
    Greeter greeter = new Greeter();
    System.out.println(greeter.sayHello());
  }
}
