package dogs;

public class Main {
  public static void main(String[] args) {
    System.out.println(Dog.bark);

    // Instantiate Dogs
    Dog dottie = new Dog("Pitbull", 10, "Black and White");
    Dog ginger = new Dog("Pomeranian", 3, "Orange");

    System.out.println(dottie.getBreed());
    System.out.println(dottie.bark);
    System.out.println(dottie.getAge());
    System.out.println(dottie.getColor());

    ginger.setBreed("mutt");
    System.out.println(ginger.getBreed());

    Dog limited = new Dog("Black");
    System.out.println(limited.getAge()); // displays 1

    Dog aDog = new Dog();
    System.out.println(aDog.getBreed()); // displays null
    aDog.setBreed("Beagles");
    System.out.println(aDog.getBreed()); // displays Beagles
  }
}