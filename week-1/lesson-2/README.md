# Lesson 2: Array Methods and String Manipulation

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

I left my campsite and hiked south for 3 miles. Then, I turned east and hiked for 3 miles. I then turned north and hiked for 3 miles, at which time I came upon a bear inside my tent eating my food! What color was the bear?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 2 - Constraints (WHERE clauses)](https://sqlbolt.com/lesson/select_queries_with_constraints)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Design HashMap](https://leetcode.com/problems/design-hashmap/description/)

### JavaScript Fundamentals (35 minutes)

- JavaScript Fundamentals (35 min): ## Arrow Functions (10 minutes)

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

1. **Arrow functions**:

   - Use for short callbacks and when you need lexical `this`
   - Avoid for object methods, constructors, and event handlers that need dynamic `this`

2. **Template literals**:
   - Use for string interpolation and multi-line strings
   - Consider tagged templates for advanced string processing

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
