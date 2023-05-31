let age = 17;
age = 18;
console.log(age);

const color = "red" // сonstants must have a value when declared and they cannot change their value

let x = 5; //whole number
let y = 8.4; //decimal
console.log(x)
console.log(y)

let count = 0;
count++;
console.log(count);

let score100 = 100;
score100--;
score100--;
console.log(score100);

// The postfix form returns the original value of the variable, and only then increments/decrements it.
let q = 5;
console.log(q++);
console.log(q);

// The prefix form increments/decrements the value, and only then returns it.
let w = 5;
console.log(++w);

let score1 = 100;
score1 = score1+10;
// or
let score2 = 100;
score2+=10;
console.log(score2);

// If you want to include a quote in a string, you need to escape it using a backslash. In this case,
// you don't need to use different enclosing quotes.
console.log('I\'m happy');
console.log("She said \"Yes!\"");

// The backslash is also used to create new lines in text. To create a new line we use \n.
console.log("One \nTwo \nThree");

// Similar to a new line, we can create a tab using \t:
console.log("\t hey \t there");

// With template literals, you can use both single and double quotes inside a string.
console.log(`I'm happy, she said "Yes"!`);

// Template literals allow multiline strings, without using \n:
let msg = `Hey! Are you sololearning?
Isn't it awesome?`;
console.log(msg);

// Template literals allow you to use variables inside the strings. You need to add a dollar sign $ and
// enclose the variable name in braces {}.
let name = "John";
let text = `Welcome, ${name}`;
console.log(text);

// Not only can we add numbers, but we can also add strings, using something called concatenation,
// which can be done on any two or more strings.
console.log("Java" + 'Script');

let isActive = true;
let isHoliday = false;
console.log(isActive);
console.log(isHoliday);

let score = 85;
console.log(score>99);

// JavaScript has a number of comparison operators:
// equal to ==
// not equal to !=
// greater than >
// smaller than <
// greater or equal to >=
// smaller or equal to <=

// Strict equality === comparison operator returns false for the values which are not of a similar type.
let x22 = 5;
let y22 = '5';
console.log(x22 == y22); //true
console.log(x22 === y22); //false

// Greater than and smaller than operators can also be used to compare strings lexicographically
// (where the alphabetical order of words is based on the alphabetical order of their component letters).
console.log('a' < 'b');
console.log("Bob" > "Dave");

let purchase = 1700;
if (purchase>=1500) {
    console.log("Discount!");
    }

let num = 12;
if(num > 5){
    console.log('Bigger than 5');
if(num < 47){
    console.log('Between 5 and 47');
    }
    }

let score_ = 98;
if(score_ >=100){
    console.log("Level Completed!");
    } else {
    console.log("Try again!");
    }

let stopLight = 'green';
if (stopLight == 'red') {
    console.log('Stop!');
    } else if (stopLight == 'yellow') {
    console.log('Slow down.');
    } else if (stopLight == 'green') {
    console.log('Go!');
    } else {
    console.log('Unknown!');
    }

let choice = 1;
switch(choice){
    case 1:
    console.log("Sports");
    break;
    case 2:
    console.log("Business");
    break;
    case 3:
    console.log("Technology");
    break;
    }

let color1 ="yellow";
switch(color1) {
    case "blue":
    console.log("This is blue.");
    break;
    case "red":
    console.log("This is red.");
    break;
    default:
    console.log("Color not found.");
    }

let age_ = 42;
let isAdult = (age_ < 18) ? "Too young": "Old enough";
console.log(isAdult);

let num_ = 2;
let isZero = (num_ == 0) ? "Zero": "Not zero";
console.log(isZero);

for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// Let's make another loop, which outputs only the even numbers from 0 to 20:
for(let i=0; i<=20; i+=2) {
  console.log(i);
}

let i = 0;
while(i<=10) {
  console.log(i);
  i++;
}

// This loop will execute the code block once, before checking if the condition is true, and then it will
// repeat the loop as long as the condition is true.
let i=5;
do {
    console.log(i);
    i++;
}
while (i<5);

// The break statement allows you to exit a loop prematurely, based on the given condition.
for(let i=0; i<10; i++) {
  if(i==3) {
    break;
  }
  console.log(i);
}


// In the same way, you can use the break statement in while loops.
let num = 1;
while(num<=10){
    if(num == 3){
        break;
    }
    console.log(num);
    num++;
}

// The continue statement is used to skip an iteration of the loop and continue from the next one.
for(let i=0;i<10;i++) {
  if(i == 5) {
    continue;
  }
  console.log(i);
}


function login() {
  console.log("Hi!");
}

function welcome(){
    let name = readLine();
    console.log('Welcome, ' + name);
}
welcome()


function login(user) {
  console.log("Hi, "+user);
}
login("james");
login("bob");

// You can use variables created outside the function as parameters:
function login(user) {
  console.log("Hi, "+user);
}
let myUser = "Bob";
login(myUser);

function discount(purchase){
    if (purchase>=1500){
        purchase*=0.85;
    }
    console.log(purchase);
}
discount(1900);
discount(1200);

// The methods we have seen so far output their result.
// In some cases, we do not need to output the result but
// need to assign it to a variable, to work with it in our program.
function add(x,y){
    return x+y;
}
let result = add(5,6);
console.log(result);

function add(x,y){
    return x+y;
    //the code below will be ignored
    console.log('Done!');
}
let result = add(5,6);
console.log(result);

