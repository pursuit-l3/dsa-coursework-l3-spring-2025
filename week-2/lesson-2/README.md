# Week 2, Lesson 2: React Props and Stack Implementation

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Probability problem

  You have three coins in a bag: a fair coin with heads and tails, a two-headed coin, and a two-tailed coin. You randomly select a coin from the bag and flip it. If the result is heads, what is the probability that you selected the two-headed coin?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 5 - Review Simple SELECT Queries](https://sqlbolt.com/lesson/select_queries_review)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### React Basics (35 minutes)

#### Understanding Props (10 minutes)

Props (short for "properties") are React's way of passing data from parent to child components. They are read-only and help make your components reusable.

**Basic Props Usage:**

```jsx
// Parent component
function App() {
  return <Greeting name="John" age={25} />;
}

// Child component
function Greeting(props) {
  return (
    <div>
      <h1>Hello, {props.name}!</h1>
      <p>You are {props.age} years old.</p>
    </div>
  );
}
```

**Props Destructuring:**

```jsx
function Greeting({ name, age }) {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
    </div>
  );
}
```

**Default Props:**

```jsx
function Greeting({ name = "Guest", age = 0 }) {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
    </div>
  );
}

// Alternative way
Greeting.defaultProps = {
  name: "Guest",
  age: 0,
};
```

#### Component Composition (15 minutes)

Component composition is a powerful pattern in React that allows you to build complex UIs by combining simpler components.

**Basic Composition:**

```jsx
function App() {
  return (
    <div>
      <Header />
      <MainContent />
      <Footer />
    </div>
  );
}

function Header() {
  return <header>This is the header</header>;
}

function MainContent() {
  return <main>This is the main content</main>;
}

function Footer() {
  return <footer>This is the footer</footer>;
}
```

**Composition with Children Props:**

```jsx
function Card({ title, children }) {
  return (
    <div className="card">
      <div className="card-header">{title}</div>
      <div className="card-body">{children}</div>
    </div>
  );
}

function App() {
  return (
    <Card title="Welcome">
      <p>This is some content inside the card.</p>
      <button>Click me</button>
    </Card>
  );
}
```

**Specialized Components:**

```jsx
function Dialog({ title, message, children }) {
  return (
    <div className="dialog">
      <h2>{title}</h2>
      <p>{message}</p>
      <div>{children}</div>
    </div>
  );
}

function WelcomeDialog() {
  return (
    <Dialog title="Welcome" message="Thank you for visiting our website!">
      <button>Get Started</button>
    </Dialog>
  );
}
```

#### Props vs. State (10 minutes)

Understanding the difference between props and state is crucial in React:

**Props:**

- Passed from parent to child components
- Read-only (immutable)
- Changes to props come from the parent component
- Used for component configuration

**State:**

- Managed within the component
- Mutable (can be changed)
- Changes to state trigger re-renders
- Used for component's internal data

**When to Use Props vs. State:**

- Use props to pass data and event handlers down to child components
- Use state to track information that the component itself needs to render properly

**Prop Drilling and Solutions:**
Prop drilling occurs when props need to be passed through multiple levels of components.

Solutions:

- Component composition
- Context API
- State management libraries (Redux, Zustand, etc.)

## Wrap-up (10 minutes)

### Component Reusability Strategies

1. **Design with Props in Mind**

   - Make components configurable through props
   - Avoid hardcoding values that could change

2. **Use Composition Patterns**

   - Leverage children props for flexible layouts
   - Create higher-order components for shared functionality

3. **Extract Reusable Logic**

   - Create custom hooks for reusable logic
   - Separate business logic from presentation

4. **Consistent Prop Naming**

   - Use clear, consistent naming conventions
   - Document props with PropTypes or TypeScript

5. **Component Libraries**
   - Consider organizing reusable components into a library
   - Use Storybook for component documentation and testing

## Additional Resources

- [React Props Documentation](https://reactjs.org/docs/components-and-props.html)
- [Composition vs Inheritance](https://reactjs.org/docs/composition-vs-inheritance.html)
- [PropTypes Documentation](https://reactjs.org/docs/typechecking-with-proptypes.html)
- [React Patterns](https://reactpatterns.com/)
