# Lesson 1: ES6+ Features

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Tower of Hanoi puzzle with 3 disks

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 1 - SELECT basics](https://sqlbolt.com/lesson/select_queries_introduction)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 minutes): [Two Sum](https://leetcode.com/problems/two-sum/)

#### Discuss Approach to the problem by going through interview process:

- Discuss the problem statement: Put the problem into your own words.
- Identify the input and output: What are the inputs? What do you need to return?
- Discuss the constraints: What are the limits on the input? Are there any edge cases?
- Check assumptions: Are there any assumptions you are making about the input?
- Discuss examples: Walk through a few examples to clarify the problem.
  - Example 1: Input: nums = [2,7,11,15], target = 9; Output: [0,1]
  - Example 2: Input: nums = [3,2,4], target = 6; Output: [1,2]
  - Example 3: Input: nums = [3,3], target = 6; Output: [0,1]
- Discuss edge cases: What if the input array is empty? What if there are no two numbers that add up to the target?
- Discuss the approach: What is your plan to solve the problem?
  - Brute Force:
    - What does brute force mean?
    - What would the brute force solution look like?
      - Using a nested loop to check each pair of numbers
      - Time complexity: O(n^2)
      - Space complexity: O(1)
  - Optimized Approach:
    - What is the optimized approach?
    - Using a hash map to store the difference between the target and each number
      - Time complexity: O(n)
      - Space complexity: O(n)
- Pseudo code your response to the prompt
  - Tips for Pseudo code:
    - Use clear variable names
    - Keep it simple and readable
    - Indent when appropriate
    - Code a complete solution, not just a snippet
- Code your solution.
- Walk through your code with an example.
- Discuss time and space complexity of your solution.

---

# Break (10 minutes)

# Getting Started (20 minutes)

### Step 1: Fork the Repository

To ensure your contributions are tracked on your GitHub profile (those valuable green squares!), you need to fork this repository properly:

1. Click the "Fork" button at the top right of this repository page
2. Select your personal GitHub account as the destination
3. Wait for the forking process to complete
4. Clone YOUR forked repository to your local machine:

```bash
git clone https://github.com/YOUR-USERNAME/dsa-coursework-l3-spring-2025.git
cd dsa-coursework-l3-spring-2025
```

5. Set up the original repository as a remote to fetch updates:

```bash
git remote add upstream https://github.com/joinpursuit/js-react-bootcamp.git
```

### Step 2: Install Dependencies

This repository uses Jest for testing. Install all dependencies:

```bash
npm install
```

### Step 3: Verify Your Setup

Run the Day 1 verification test to make sure everything is set up correctly:

```bash
npm run test setup-test.js
```

You should see a passing test confirming your environment is ready!

## Repository Structure

Each day's folder contains:

- Exercise files (JavaScript or JSX) where you'll write your code
- Test files that verify your solutions
- A README with specific instructions for that day

## Day 1 Agenda: Environment Setup & JavaScript Fundamentals

Today's goals:

1. Successfully fork and set up the repository
2. Ensure tests run correctly
3. Complete basic JavaScript variable exercises

### Day 1 Exercises

Navigate to the `week-1/lesson-1/exercises/` directory and complete the following:

1. `variables.js` - Practice with `let` and `const`

Run tests for individual exercises:

```bash
# Test a specific exercise
npm test -- week-1/lesson-1/__tests__/variables.test.js
```

## How to Submit Your Work

After completing each day's exercises:

1. Commit your changes:

```bash
git add .
git commit -m "Completed Day X exercises"
```

2. Push to your forked repository:

```bash
git push origin main
```

1. Variable declarations with `let` and `const`
2. Arrow functions
3. Template literals

Let's dive into each of these features and understand how they improve our JavaScript code.

## Variable Declarations with `let` and `const` (25 minutes)

### The Problem with `var`

https://www.youtube.com/shorts/ZRjmGq1gAEQ

Before ES6, JavaScript had only one way to declare variables: the `var` keyword. However, `var` had several issues:

```javascript
// Function scope vs. block scope

function varExample() {
  let x = 1;
  console.log(x); // 1

  if (true) {
    let x = 2; // Same variable!
    console.log(x); // 2
  }

  console.log(x); // 1 - the value changed
}

// Hoisting issues
function hoistingExample() {
  console.log(hoisted); // undefined (not an error)
  var hoisted = "This variable was hoisted";
}
```

### Introducing `let`

ES6 introduced `let`, which provides block scoping:

```javascript
function letExample() {
  let x = 1;

  if (true) {
    let x = 2; // Different variable
    console.log(x); // 2
  }

  console.log(x); // 1 - original value preserved
}

// Temporal Dead Zone
function temporalDeadZone() {
  // console.log(notHoisted);  // ReferenceError
  let notHoisted = "This variable is not hoisted";
}
```

### Introducing `const`

For values that shouldn't change, ES6 introduced `const`:

```javascript
// Basic const usage
const PI = 3.14159;
// PI = 3.14;  // TypeError: Assignment to constant variable

// const with objects
const person = { name: "John" };
person.name = "Jane"; // This works! Only the reference is constant
// person = { name: "Jane" };  // TypeError: Assignment to constant variable

// const with arrays
const numbers = [1, 2, 3];
numbers.push(4); // This works!
// numbers = [1, 2, 3, 4];  // TypeError: Assignment to constant variable
```

### Best Practices

- Use `const` by default
- Use `let` when you need to reassign a variable
- Avoid `var` in modern code
- Declare variables at the top of their scope

## Arrow Functions (10 minutes)

### Traditional Functions vs. Arrow Functions

Traditional function declarations can be verbose:

```javascript
// Traditional function expression
const add = function (a, b) {
  return a + b;
};

// Traditional method in an object
const calculator = {
  value: 0,
  add: function (a, b) {
    return a + b;
  },
};

calculator.add(5, 10); // 15
```

Arrow functions provide a more concise syntax:

```javascript
// Basic arrow function
const add = (a, b) => {
  return a + b;
};

// Even more concise with implicit return
const add = (a, b) => a + b;

// Single parameter (parentheses optional)
const square = (x) => x * x;

// No parameters require empty parentheses
const getRandomNumber = () => Math.random();
```

### Lexical `this`

One of the most powerful features of arrow functions is how they handle the `this` keyword:

```javascript
// Traditional function - 'this' problem
function Counter() {
  this.count = 0;

  setInterval(function () {
    // 'this' here refers to the global object, not Counter
    this.count++;
    console.log(this.count); // NaN
  }, 1000);
}

// Traditional workaround
function Counter() {
  this.count = 0;
  const self = this;

  setInterval(function () {
    self.count++;
    console.log(self.count); // Works as expected
  }, 1000);
}

// Arrow function solution
function Counter() {
  this.count = 0;

  setInterval(() => {
    // 'this' is lexically bound to Counter
    this.count++;
    console.log(this.count); // Works as expected
  }, 1000);
}
```

### When Not to Use Arrow Functions

Arrow functions are not always the best choice:

```javascript
// Object methods (where 'this' should refer to the object)
const person = {
  name: "Alice",
  // Bad practice with arrow function
  greet: () => {
    console.log(`Hello, my name is ${this.name}`); // 'this' is not bound to person
  },
  // Good practice with method syntax
  greet() {
    console.log(`Hello, my name is ${this.name}`); // Works correctly
  },
};

// Constructor functions
// Arrow functions cannot be used as constructors
// const Person = (name) => { this.name = name; };  // Doesn't work
// const alice = new Person("Alice");  // TypeError

// Event handlers that need to use 'this' to refer to the DOM element
button.addEventListener("click", function () {
  this.classList.toggle("active"); // 'this' refers to the button
});
```

## Template Literals (5 minutes)

### Basic Syntax

Template literals provide an improved way to work with strings:

```javascript
// Traditional string concatenation
const name = "Alice";
const greeting = "Hello, " + name + "!";

// Template literal
const betterGreeting = `Hello, ${name}!`;

// Multi-line strings
// Traditional (cumbersome)
const oldMultiline =
  "This is line 1.\n" + "This is line 2.\n" + "This is line 3.";

// With template literals
const multiline = `This is line 1.
This is line 2.
This is line 3.`;
```

### Expression Interpolation

Template literals can include any JavaScript expression:

```javascript
const a = 5;
const b = 10;
console.log(`Sum: ${a + b}, Product: ${a * b}`);

const person = { name: "Bob", age: 25 };
console.log(`${person.name} is ${person.age} years old.`);

// Can include function calls
const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1);
console.log(`${capitalize("hello")} world!`);

// Can include conditional expressions
const status = 18;
console.log(`Status: ${status >= 18 ? "Adult" : "Minor"}`);
```

### Tagged Templates

Template literals can be processed by a tag function:

```javascript
function highlight(strings, ...values) {
  return strings.reduce((result, string, i) => {
    return (
      result +
      string +
      (values[i] ? `<span class="highlight">${values[i]}</span>` : "")
    );
  }, "");
}

const name = "Alice";
const age = 28;
const highlighted = highlight`${name} is ${age} years old.`;
// Result: "<span class="highlight">Alice</span> is <span class="highlight">28</span> years old."
```

## Practical Examples (5 minutes)

Let's see how these features work together in practical scenarios:

```javascript
// Data processing example
const users = [
  { id: 1, name: "Alice", age: 28 },
  { id: 2, name: "Bob", age: 35 },
  { id: 3, name: "Charlie", age: 22 },
];

// ES5 way
var adultNamesES5 = users
  .filter(function (user) {
    return user.age >= 18;
  })
  .map(function (user) {
    return user.name;
  });

// ES6+ way
const adultNames = users
  .filter((user) => user.age >= 18)
  .map((user) => user.name);

console.log(`Adult users: ${adultNames.join(", ")}`);

// DOM manipulation example
const todoItems = [
  { id: 1, text: "Learn JavaScript", completed: true },
  { id: 2, text: "Build a project", completed: false },
];

const renderTodoList = () => {
  const todoList = document.getElementById("todo-list");

  todoList.innerHTML = todoItems
    .map(
      (item) => `
      <li class="${item.completed ? "completed" : ""}">
        <input 
          type="checkbox" 
          ${item.completed ? "checked" : ""}
          data-id="${item.id}"
        />
        ${item.text}
      </li>
    `
    )
    .join("");
};
```

## Conclusion and Best Practices (5 minutes)

To summarize what we've learned:

1. **Variable declarations**:

   - Use `const` by default
   - Use `let` when reassignment is necessary
   - Avoid `var` in modern code

These ES6+ features have greatly improved JavaScript development, making code more concise, readable, and less prone to common errors. As you practice using these features, you'll develop an intuition for when each one is most appropriate.

In our next session, we'll explore more advanced ES6+ features like destructuring, spread/rest operators, and modules.

For practice:

1. Refactor a traditional JavaScript function to use arrow functions
2. Convert string concatenation to template literals
3. Replace `var` declarations with appropriate `let` or `const`

Any questions before we move on?

## Wrap-up (10 minutes)

- Wrap-up (10 min): Solution review and implementation alternatives

## Additional Resources
