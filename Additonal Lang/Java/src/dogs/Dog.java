package dogs;

public class Dog {
  public static String bark = "Woof!";

  private String breed;
  private int age;
  private String color;

  // default constructor
  public Dog(){ }

  // Limited initial state
  public Dog(String color) {
    this.breed = "Mutt";
    this.age = 1;
    this.color = color;
  }

  public Dog(String breed, int age, String color) {
    this.breed = breed;
    this.age = age;
    this.color = color;
  }

  // Read state, Accessors (Getters)
  public String getBreed() {
    return breed;
  }

  public int getAge() {
    return age;
  }

  public String getColor() {
    return color;
  }

  // Change state, Mutators (setters)
  public void setBreed(String breed) {
    this.breed = breed;
  }

  public void setAge(int age) {
    this.age = age;
  }

  public void setColor(String color) {
    this.color = color;
  }

  // Other methods
  public void sleep(int minutes) {
    System.out.println("ZZZ " + minutes);
  }
}