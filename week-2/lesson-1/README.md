# Week 2, Lesson 1: React Basics and Queue Implementation

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Logical sequence completion

  What comes next in this sequence? 1, 11, 21, 1211, 111221, ?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 4 - Filtering and sorting Query results](https://sqlbolt.com/lesson/filtering_sorting_query_results)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

### React Basics (35 minutes)

#### Introduction to React (5 minutes)

React is a JavaScript library for building user interfaces, particularly single-page applications. It was developed by Facebook and is now maintained by Facebook and a community of individual developers and companies.

**Key Features of React:**

- Component-based architecture
- Virtual DOM for efficient rendering
- Declarative approach to building UIs
- Unidirectional data flow
- Rich ecosystem and community support

#### Setting Up a React Project (5 minutes)

There are several ways to create a React application:

**Using Create React App (CRA):**

```bash
npx create-react-app my-app
cd my-app
npm start
```

**Using Vite (faster alternative):**

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

#### Component Structure and JSX (15 minutes)

**What is JSX?**
JSX (JavaScript XML) is a syntax extension for JavaScript that looks similar to HTML but allows you to write HTML-like code in your JavaScript files.

**Basic Component Structure:**

```jsx
import React from "react";

function Greeting(props) {
  return (
    <div className="greeting">
      <h1>Hello, {props.name}!</h1>
      <p>Welcome to React.</p>
    </div>
  );
}

export default Greeting;
```

**JSX Rules and Syntax:**

- JSX elements must have a closing tag or be self-closing
- Components must return a single root element (or use fragments)
- JavaScript expressions can be included using curly braces `{}`
- HTML attributes use camelCase naming (e.g., `className` instead of `class`)
- Inline styles are defined as objects with camelCase properties

**Class Components vs. Function Components:**

Function Component:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

Class Component:

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

**Note:** Modern React development favors function components with hooks over class components.

#### Rendering Elements and Components (10 minutes)

**Rendering Elements:**

```jsx
import React from "react";
import ReactDOM from "react-dom/client";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<h1>Hello, world!</h1>);
```

**Rendering Components:**

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
```

**Conditional Rendering:**

```jsx
function UserGreeting(props) {
  return (
    <div>
      {props.isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign in.</h1>}
    </div>
  );
}
```

**Rendering Lists:**

```jsx
function NumberList(props) {
  const numbers = props.numbers;
  const listItems = numbers.map((number) => (
    <li key={number.toString()}>{number}</li>
  ));

  return <ul>{listItems}</ul>;
}
```

## Wrap-up (10 minutes)

### Component Design Principles

1. **Single Responsibility Principle**

   - Each component should ideally do one thing well
   - If a component grows too large, consider breaking it down

2. **Composition Over Inheritance**

   - React favors component composition rather than inheritance hierarchies
   - Use props and children to build flexible components

3. **Reusability**

   - Design components to be reusable when possible
   - Avoid hardcoding values that could be passed as props

4. **Separation of Concerns**

   - Separate UI logic from business logic
   - Consider using container and presentational component patterns

5. **Naming Conventions**
   - Use PascalCase for component names
   - Use descriptive names that indicate the component's purpose

## Additional Resources

- [React Official Documentation](https://reactjs.org/docs/getting-started.html)
- [Create React App Documentation](https://create-react-app.dev/docs/getting-started)
- [React DevTools for Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)
- [React DevTools for Firefox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)
