package interfaces;

public class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();
    Dog myDog = new Dog();

    myPig.animalSound();
    myPig.sleep();

    myDog.animalSound();
    myDog.sleep();
    myDog.eat();
  }
}