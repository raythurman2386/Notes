package interfaces;

public class Dog implements Animal {
  @Override public void animalSound() {
    System.out.println("Woof");
  }

  @Override public void sleep() {
    System.out.println("Snore. . .");
  }

  public void eat() {
    System.out.println("chomp chomp chomp");
  }
}