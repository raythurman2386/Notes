// TS Types and How to use them
// Explicit types
const isOpen: boolean = false;

const myName: string = "Ray";

const myAge: number = 30;

const list: number[] = [1, 2, 3];

const strList: string[] = ["something", "else", "here"]

const me: [string, number, boolean] = ["Ray", 32, false];

enum Job { WebDev, WebDesigner, PM }
const job: Job = Job.WebDev;

const phone: any = "Pixel 3";
const tablet: any = 3;

// Functions in TS
// ? is for optional params
const sayWord = (word?: string): string => {
  console.log(word || "Hello");
  return word || "Hello";
};

// Default params
const saySomething = (word = "Hello", ...otherStuff: string[]): string => {
  console.log(otherStuff);
  console.log(word);
  return word;
};

sayWord("Ray");

// TS Knows this should be a string
// AKA Implicit Type
let newName = 'Raymond';
newName = 10;

// Union Types with |
let anotherNewName: string | number = 'Raymond';
anotherNewName = 3;

const makeMargin = (x: string | number): string => {
  return `margin: ${x}px;`
}

makeMargin(10);
makeMargin('10');
// makeMargin(true);

// Null types
// Gotcha
let dog: string = 'Layla';
dog = null;
dog = "Zeus";
dog = undefined;
// dog = 10;
// dog = false;

// Interface
interface Person {
  name: string,
  age?: number // Optional Param
}

const sayName = ({ name, age }: Person): string => {
  console.log(name);
  return name;
}

sayName({ name: 'Ray', age: 30 })

sayName({ age: 29, name: 'Sheryl' })

// Enums
// Num Enum
enum Type {
  Video,
  BlogPost,
  Quiz
}

// String Enum
enum Type2 {
  Video = "VIDEO",
  BlogPost = "BLOG_POST",
  Quiz = "QUIZ"
}

const createContent = (contentType: Type) => { }
createContent(Type.Video)

console.log(Type.Quiz); // 2, console logs the index of Quiz
console.log(Type2.Video); // VIDEO, 