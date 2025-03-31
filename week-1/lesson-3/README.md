# Lesson 3: Asynchronous JavaScript and Hash Implementation

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Can you name the three playing cards that have been place in a row using the following clues? There is a two to the right of a king. A diamond will be found to the left of a spade. An ace is to the left of a heart. A heart is to the left of a spade.

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 3 - SQL Queries with constraints](https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

### Session 2: Advanced HashMap Features and Testing

Review and Continue (10 minutes)

Review progress from Session 1
Address common challenges and questions
Set goals for Session 2

Advanced Implementation (25 minutes)

This should be completed using the starter code provided in the previous session.

Complete the remaining operations:

Search/lookup functionality
Delete operation
Resize/rehash when load factor increases
Improved collision resolution strategy

Testing and Review (10 minutes)

Run test cases to verify correctness
Analyze performance
Discuss real-world applications

JavaScript Fundamentals: Asynchronous JavaScript (35 minutes)
Introduction (5 minutes)
JavaScript is single-threaded, which means it can only execute one piece of code at a time. However, many operations like fetching data from a server, reading files, or waiting for user input take time. Asynchronous programming allows JavaScript to handle these operations without blocking the main thread.
Today, we'll explore:

The evolution of asynchronous JavaScript
Promises and their methods
Async/await syntax
Error handling in asynchronous code
Practical examples and patterns

Let's start by understanding the problem that asynchronous JavaScript solves.
The Problem: Callback Hell (5 minutes)
Before modern asynchronous features, JavaScript relied on callbacks:
javascriptCopy// Traditional callback approach
function fetchUserData(userId, callback) {
// Simulate API request
setTimeout(() => {
const user = { id: userId, name: "John Doe" };
callback(user);
}, 1000);
}

fetchUserData(123, function(user) {
console.log(`Found user: ${user.name}`);

fetchUserPosts(user.id, function(posts) {
console.log(`${user.name} has ${posts.length} posts`);

    fetchPostComments(posts[0].id, function(comments) {
      console.log(`First post has ${comments.length} comments`);

      // More nested callbacks...
    });

});
});
This leads to deeply nested code known as "callback hell" or the "pyramid of doom." This code is:

Hard to read and maintain
Difficult to reason about
Challenging for error handling
Sequential by nature

Promises: A Better Way (10 minutes)
Promises represent the eventual completion (or failure) of an asynchronous operation and its resulting value.
Creating Promises
javascriptCopy// Creating a promise
const myPromise = new Promise((resolve, reject) => {
// Asynchronous operation
setTimeout(() => {
const success = true;

    if (success) {
      resolve("Operation completed successfully!");
    } else {
      reject(new Error("Operation failed!"));
    }

}, 1000);
});

// Using a promise
myPromise
.then(result => {
console.log(result); // "Operation completed successfully!"
})
.catch(error => {
console.error(error);
});
Promise States
A Promise can be in one of three states:

Pending: Initial state, neither fulfilled nor rejected
Fulfilled: The operation completed successfully
Rejected: The operation failed

Promise Chaining
javascriptCopy// Refactoring our previous example with promises
function fetchUserData(userId) {
return new Promise((resolve, reject) => {
setTimeout(() => {
const user = { id: userId, name: "John Doe" };
resolve(user);
}, 1000);
});
}

function fetchUserPosts(userId) {
return new Promise((resolve, reject) => {
setTimeout(() => {
const posts = [
{ id: 1, title: "First Post" },
{ id: 2, title: "Second Post" }
];
resolve(posts);
}, 1000);
});
}

// Using promise chaining
fetchUserData(123)
.then(user => {
console.log(`Found user: ${user.name}`);
return fetchUserPosts(user.id);
})
.then(posts => {
console.log(`User has ${posts.length} posts`);
return posts[0];
})
.then(firstPost => {
console.log(`First post title: ${firstPost.title}`);
})
.catch(error => {
console.error("Something went wrong:", error);
});
Promise Methods
javascriptCopy// Promise.all - wait for all promises to resolve
const promise1 = Promise.resolve(3);
const promise2 = new Promise(resolve => setTimeout(() => resolve("foo"), 100));
const promise3 = fetch('https://jsonplaceholder.typicode.com/users');

Promise.all([promise1, promise2, promise3])
.then(values => {
console.log(values); // [3, "foo", Response]
});

// Promise.race - resolves or rejects as soon as one promise resolves/rejects
Promise.race([
new Promise(resolve => setTimeout(() => resolve("fast"), 100)),
new Promise(resolve => setTimeout(() => resolve("slow"), 500))
])
.then(result => {
console.log(result); // "fast"
});

// Promise.allSettled - wait for all promises to settle (resolve or reject)
Promise.allSettled([
Promise.resolve(1),
Promise.reject(new Error("Error")),
Promise.resolve(3)
])
.then(results => {
console.log(results);
// [{status: "fulfilled", value: 1},
// {status: "rejected", reason: Error},
// {status: "fulfilled", value: 3}]
});
Async/Await: Elegant Asynchronous Code (10 minutes)
Async/await is syntactic sugar over promises, making asynchronous code look and behave more like synchronous code.
Basic Syntax
javascriptCopy// Function declaration with async
async function fetchData() {
const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
const data = await response.json();
return data;
}

// Arrow function with async
const fetchData = async () => {
const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
const data = await response.json();
return data;
};

// Using the async function
fetchData()
.then(data => console.log(data))
.catch(error => console.error(error));
Rewriting Promise Chains
javascriptCopy// Previous promise chain example using async/await
async function getUserDetails(userId) {
try {
const user = await fetchUserData(userId);
console.log(`Found user: ${user.name}`);

    const posts = await fetchUserPosts(user.id);
    console.log(`User has ${posts.length} posts`);

    const firstPost = posts[0];
    console.log(`First post title: ${firstPost.title}`);

    return { user, posts };

} catch (error) {
console.error("Something went wrong:", error);
throw error; // Rethrow or handle as needed
}
}

// Call the async function
getUserDetails(123)
.then(result => {
console.log("All data fetched successfully!");
})
.catch(error => {
console.error("Failed to get user details");
});
Parallel Execution with Async/Await
javascriptCopyasync function fetchMultipleResources() {
try {
// Sequential execution (slower)
console.time('sequential');
const users = await fetch('https://jsonplaceholder.typicode.com/users').then(r => r.json());
const posts = await fetch('https://jsonplaceholder.typicode.com/posts').then(r => r.json());
console.timeEnd('sequential');

    // Parallel execution (faster)
    console.time('parallel');
    const [parallelUsers, parallelPosts] = await Promise.all([
      fetch('https://jsonplaceholder.typicode.com/users').then(r => r.json()),
      fetch('https://jsonplaceholder.typicode.com/posts').then(r => r.json())
    ]);
    console.timeEnd('parallel');

    return { users, posts };

} catch (error) {
console.error('Error fetching resources:', error);
}
}
Error Handling Patterns (5 minutes)
Try/Catch with Async/Await
javascriptCopyasync function fetchDataSafely(url) {
try {
const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    return data;

} catch (error) {
console.error('Fetch error:', error);
// Handle different types of errors
if (error.name === 'TypeError') {
// Network error or CORS issue
return { error: 'Network error', details: error.message };
} else {
// Other errors
return { error: 'Unknown error', details: error.message };
}
}
}
Higher-Order Function for Error Handling
javascriptCopy// Utility function to handle async errors
function handleAsyncError(asyncFn) {
return async function(...args) {
try {
return await asyncFn(...args);
} catch (error) {
console.error('Error in async function:', error);
// Additional error handling logic
return null;
}
};
}

// Usage
const safeFetch = handleAsyncError(async (url) => {
const response = await fetch(url);
return response.json();
});

// Now you can use it without try/catch
safeFetch('https://jsonplaceholder.typicode.com/todos/1')
.then(data => {
if (data) {
console.log('Data:', data);
} else {
console.log('Failed to fetch data');
}
});
Real-World Example: Building a Countdown Timer (5 minutes)
Let's put our knowledge to work by building a countdown timer using promises and async/await:
javascriptCopyfunction delay(ms) {
return new Promise(resolve => setTimeout(resolve, ms));
}

async function countdown(seconds) {
console.log(`Countdown starting from ${seconds} seconds`);

for (let i = seconds; i > 0; i--) {
console.log(`${i}...`);
await delay(1000);
}

console.log("Countdown complete!");
return "Done";
}

// Basic usage
countdown(5)
.then(result => console.log(result))
.catch(error => console.error(error));

// With cancellation capability
function createCancellableCountdown(seconds) {
let isCancelled = false;

const promise = (async () => {
console.log(`Countdown starting from ${seconds} seconds`);

    for (let i = seconds; i > 0; i--) {
      if (isCancelled) {
        throw new Error("Countdown cancelled");
      }

      console.log(`${i}...`);
      await delay(1000);
    }

    console.log("Countdown complete!");
    return "Done";

})();

return {
promise,
cancel: () => { isCancelled = true; }
};
}

// Usage with cancellation
const { promise, cancel } = createCancellableCountdown(10);

// Cancel after 3 seconds
setTimeout(() => {
console.log("Cancelling countdown...");
cancel();
}, 3000);

promise
.then(result => console.log(result))
.catch(error => console.log(error.message));
Wrap-up and Practice Ideas (5 minutes)
We've covered a lot about asynchronous JavaScript:

The evolution from callbacks to promises to async/await
Creating and consuming promises
Error handling patterns
Practical applications

For practice, try:

Convert a callback-based API to use promises
Implement a retry mechanism for failed API calls
Build a function that fetches data from multiple endpoints in parallel
Create a timeout wrapper for promises that might take too long

Key Takeaways:

Promises provide a cleaner alternative to nested callbacks
Async/await makes asynchronous code even more readable
Always handle errors in asynchronous code
Choose between sequential and parallel execution based on your needs

Resources for Further Learning:

MDN Web Docs: Promises https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
MDN Web Docs: Async functions https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
JavaScript.info: Async/await https://javascript.info/async-await

Any questions before we move on?

## Wrap-up (10 minutes)

- Wrap-up (10 min): Common pitfalls and best practices

## Additional Resources
