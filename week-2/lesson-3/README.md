# Week 2, Lesson 3: React State Management

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Cryptarithmetic puzzle

  Solve this cryptarithmetic puzzle where each letter represents a unique digit:

  ```
  SEND
  +MORE
  -----
  MONEY
  ```

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 6 - Multi-table queries with JOINs](https://sqlbolt.com/lesson/select_queries_with_joins)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### React State (35 minutes)

#### Introduction to State in React (5 minutes)

State is a built-in feature in React that allows components to create and manage their own data. Unlike props (which are passed from parent to child), state is internal to a component.

**Key Characteristics of State:**

- State is mutable (can be updated)
- Changes to state trigger re-renders
- State updates may be asynchronous
- State should be treated as immutable when updating it

#### The useState Hook (10 minutes)

The `useState` hook is the primary way to add state to functional components in React.

**Basic Usage:**

```jsx
import React, { useState } from "react";

function Counter() {
  // Declare a state variable 'count' with initial value 0
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}
```

**Multiple State Variables:**

```jsx
function UserForm() {
  const [name, setName] = useState("");
  const [age, setAge] = useState(0);
  const [email, setEmail] = useState("");

  return (
    <form>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Name"
      />
      <input
        type="number"
        value={age}
        onChange={(e) => setAge(Number(e.target.value))}
        placeholder="Age"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
    </form>
  );
}
```

**Using Objects with useState:**

```jsx
function UserForm() {
  const [user, setUser] = useState({
    name: "",
    age: 0,
    email: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser({
      ...user, // Important: spread the existing state
      [name]: value, // Update only the changed field
    });
  };

  return (
    <form>
      <input
        type="text"
        name="name"
        value={user.name}
        onChange={handleChange}
        placeholder="Name"
      />
      <input
        type="number"
        name="age"
        value={user.age}
        onChange={handleChange}
        placeholder="Age"
      />
      <input
        type="email"
        name="email"
        value={user.email}
        onChange={handleChange}
        placeholder="Email"
      />
    </form>
  );
}
```

#### State Updates and Rendering (10 minutes)

**State Updates are Asynchronous:**

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  // This may not work as expected
  const incrementTwice = () => {
    setCount(count + 1); // Uses current state value
    setCount(count + 1); // Also uses the same current state value
  };

  // This works correctly
  const incrementTwiceCorrectly = () => {
    setCount((prevCount) => prevCount + 1); // Uses previous state
    setCount((prevCount) => prevCount + 1); // Uses updated previous state
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={incrementTwice}>Increment Twice (Wrong)</button>
      <button onClick={incrementTwiceCorrectly}>
        Increment Twice (Correct)
      </button>
    </div>
  );
}
```

**State and Re-rendering:**

- React components re-render when their state or props change
- Only the component and its children re-render, not the entire application
- React uses a virtual DOM to optimize actual DOM updates

#### Lifting State Up (10 minutes)

When multiple components need to share state, you can "lift the state up" to their closest common ancestor.

```jsx
function ParentComponent() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <h1>Count: {count}</h1>
      <ChildA count={count} />
      <ChildB onIncrement={increment} />
    </div>
  );
}

function ChildA({ count }) {
  return <p>The current count is: {count}</p>;
}

function ChildB({ onIncrement }) {
  return <button onClick={onIncrement}>Increment</button>;
}
```

**Benefits of Lifting State Up:**

- Single source of truth for shared data
- Easier to debug and maintain
- Avoids prop drilling for deeply nested components (to some extent)

## Wrap-up (10 minutes)

### State Update Best Practices

1. **Treat State as Immutable**

   - Always create new objects/arrays when updating state
   - Use spread operators or methods like `map`, `filter`, and `reduce`
   - Never directly modify state objects

2. **Use Functional Updates for Derived State**

   ```jsx
   // Instead of this:
   setCount(count + 1);

   // Do this:
   setCount((prevCount) => prevCount + 1);
   ```

3. **Keep State Minimal and Flat**

   - Don't store derived data that can be calculated from props or other state
   - Avoid deeply nested state objects
   - Consider normalizing complex state structures

4. **Separate Related State Logic**

   - Use multiple `useState` calls for unrelated state
   - Consider using `useReducer` for complex state logic
   - Create custom hooks to encapsulate related state logic

5. **State Initialization Patterns**
   - Use lazy initialization for expensive computations
   ```jsx
   // Lazy initialization
   const [state, setState] = useState(() => {
     // This function runs only on initial render
     return computeExpensiveInitialState();
   });
   ```

## Additional Resources

- [React State and Lifecycle Documentation](https://reactjs.org/docs/state-and-lifecycle.html)
- [Hooks API Reference](https://reactjs.org/docs/hooks-reference.html)
- [Thinking in React](https://reactjs.org/docs/thinking-in-react.html)
- [A Complete Guide to useEffect](https://overreacted.io/a-complete-guide-to-useeffect/)
