package interfaces;

class Pig implements Animal {
  @Override public void animalSound() {
    System.out.println("Oink Oink");
  }

  @Override public void sleep() {
    System.out.println("ZZZ");
  }
}