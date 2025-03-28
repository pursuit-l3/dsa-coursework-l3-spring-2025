# Pursuit L3 V3 Spring 2025 Techncial Interview Training Coursework

Welcome to Pursuit L3 V3 Spring 2025 Techncial Interview Training! This repository contains all the materials you'll need throughout the program, including practice exercises, challenges, and tests to verify your solutions.

## Getting Started (Day 1)

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
git remote add upstream https://github.com/ORIGINAL-OWNER/js-react-bootcamp.git
```

### Step 2: Install Dependencies

This repository uses Jest for testing. Install all dependencies:

```bash
npm install
```

### Step 3: Verify Your Setup

Run the Day 1 verification test to make sure everything is set up correctly:

```bash
npm run test:day1
```

You should see a passing test confirming your environment is ready!

## Repository Structure

```
js-react-bootcamp/
├── days/
│   ├── day1/
│   │   ├── exercises/         # Practice exercises
│   │   ├── __tests__/         # Test files
│   │   └── README.md          # Day 1 instructions
│   ├── day2/
│   │   └── ...
│   └── ...
├── package.json
└── README.md
```

Each day's folder contains:

- Exercise files (JavaScript or JSX) where you'll write your code
- Test files that verify your solutions
- A README with specific instructions for that day

## Day 1 Agenda: Environment Setup & JavaScript Fundamentals

Today's goals:

1. Successfully fork and set up the repository
2. Ensure tests run correctly
3. Complete basic JavaScript exercises
4. Review ES6+ features you'll be using throughout the bootcamp

### Day 1 Exercises

Navigate to the `week-1/lesson-1/exercises/` directory and complete the following:

1. `variables.js` - Practice with `let` and `const`
2. `functions.js` - Arrow functions and basic function concepts
3. `arrays.js` - Array methods like map, filter, and reduce
4. `objects.js` - Object destructuring and manipulation

Run tests for individual exercises:

```bash
# Test a specific exercise
npm test -- days/day1/__tests__/variables.test.js

# Run all Day 1 tests
npm run test:day1
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

3. Your green squares will be updated on your GitHub profile!

## Staying Up-to-Date

If we update the main repository with new content:

```bash
git fetch upstream
git merge upstream/main
```

## Setting Up for Success

- **Commit often**: Small, frequent commits create more green squares and show your progress
- **Read the tests**: Understanding what the tests expect helps solve the exercises
- **Ask questions**: Use the group chat if you're stuck
- **Review documentation**: Links to relevant docs are provided in each day's README

Ready to begin? Head to `days/day1/README.md` for your first day's detailed instructions!

Happy coding!
