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

# Course Outline

## L3 V3 Spring 2025 Course Outline

## Introduction

The L3 V3 Spring 2025 program represents a comprehensive technical curriculum. Through an immersive, project-based approach, fellows will develop proficiency across the entire software development lifecycle while building a robust foundation in algorithms, cybersecurity, full-stack development, as well as proficiency in java and python.

This intensive 11-week program follows a carefully structured progression that balances theoretical knowledge with hands-on application. Fellows will work on increasingly complex projects that mirror real-world development scenarios, culminating in demonstrable skills that directly translate to workplace demands.

## Course Description

This course will be conducted 3 days a week for 11 weeks, with each day incorporating daily practice in algorithm solving, cybersecurity principles, full-stack implementation, and Java/Python programming. The program is designed to progressively build and reinforce knowledge through practical application and targeted exercises.

The course is centered around building a comprehensive application portfolio that demonstrates mastery across various technology stacks while emphasizing industry best practices in security, efficiency, and collaboration.

### Daily Template

#### Early Afternoon Session (2 hours)

- Warm-up (20 min)
- Brain Teaser (10 min): Logic or pattern recognition challenge
- SQL Exercise (10 min): Database concept reinforcement
- Technical Training (90 min)
  - Solving Interview Questions using Python
  - Data Structures and Algorithms deep dives
- Wrap-up (10 min)
  - Solution review and knowledge consolidation
  - Daily progress tracking

#### Afternoon Session (2 hours)

- Task Introduction / Stand Up (15 - 30 min)
- Check in with fellows on progress, goals and blockers
- Building (1.5 - 1.75 hours)
- Hands-on implementation time
- Technical requirement implementation
- Instructor-guided troubleshooting

# Proposed Project Progression

## Project 1: Personal Portfolio Website

Tech Stack: HTML/CSS, JavaScript
Purpose: Serve as a digital resume and portfolio for future projects
Focus: Clean design, semantic markup, responsive layout
Timeline: Weeks 1-3

## Project 2: E-Commerce Web Application

Tech Stack: React (frontend), Express/Node.js (backend), MongoDB
Features: User authentication, nested routes, state management, AI-powered search
Focus: Full-stack integration, component-driven development, backend API design, frontend interaction
Timeline: Weeks 4-7

## Project 3: Cybersecurity-Focused Infrastructure Project

Tech Stack: Python, networking tools, Linux, cloud services
Goal: Create a VLAN to segment home network traffic for guests vs. personal devices
Focus: Applied cybersecurity, networking fundamentals, system design
Timeline: Weeks 8-11
Detailed 3-Week Schedule (First Module)
Week 1: Python Fundamentals & DSA Basics

## Proposed Daily Outline

## Week 1

### Day 1

- Technical Training: Python fundamentals, data types, control structures
- DSA Focus: Arrays and lists in Python
- Project Work: Portfolio wireframing, repository setup, Git workflow introduction
- Cybersecurity Focus: Web security basics, HTTPS, content security policies

### Day 2

- Technical Training: Python functions, error handling, list comprehensions
- DSA Focus: String manipulation
  Project Work: Implementing basic page structure, navigation design using HTML/CSS

### Day 3

- Technical Training: Python modules, libraries, virtual environments
- DSA Focus: Hash Tables
- Project Work: Mobile-first implementation of portfolio layout

## Week 2: Advanced Data Structures & Portfolio Development

### Day 4

- Technical Training: Object-oriented programming in Python
- DSA Focus: Stacks
- Project Work: Interactive elements for portfolio, animations
  Cybersecurity Focus: Input validation, XSS prevention

### Day 5

- Technical Training: Recursion and memoization techniques
- DSA Focus: Linked lists (LeetCode problems: Reverse Linked List, Merge Two Sorted Lists)
- Project Work: Styling refinement, accessibility implementation

### Day 6

- Technical Training: Algorithmic complexity (Big O notation)
  DSA Focus: Binary search (LeetCode problems: Binary Search, Find First and Last Position)
- Project Work: Image optimization, performance auditing
  Java Exercise: OOP principles through simple Java examples
  Week 3: Advanced Algorithms & Portfolio Completion

### Day 7

- Technical Training: Dynamic programming fundamentals
- DSA Focus: Classic DP problems (LeetCode problems: Climbing Stairs, Coin Change)
- Project Work: Contact form implementation, portfolio content development

### Day 8

- Technical Training: Graph algorithms and representations
- DSA Focus: BFS/DFS implementations (LeetCode problems: Number of Islands, Course Schedule)
- Project Work: Setting up automated deployment, testing
- Cybersecurity Focus: Secure deployment practices

### Day 9

- Technical Training: Advanced algorithm patterns and techniques
- DSA Focus: Comprehensive review and mock interview practice
- Project Work: Final refinements, peer review session
- Assessment: Algorithm proficiency test and portfolio project presentations

### Capstone Opportunity

Top-performing students will be invited to interview with a senior instructor for a collaborative research project: an AI agent designed to teach coding. This project will emphasize cutting-edge AI integration and provide an opportunity to work on a live, impactful product.

## Learning Outcomes

Students completing this program will:

- Master fundamental data structures and algorithms used in technical interviews
- Develop advanced problem-solving skills through daily LeetCode-style challenges
- Analyze algorithmic time and space complexity with confidence
- Be proficient in Python for both algorithmic problem-solving and application development
- Understand core Java concepts for versatile language capabilities
- Navigate git workflows and collaborative software development efficiently
- Communicate effectively in technical stand-ups and code reviews
- Demonstrate real-world readiness through polished projects and strong CS fundamentals
- Develop a security-first mindset when approaching technical problems
- Successfully tackle medium to hard interview questions at top technology companies
- This immersive, modular approach ensures that graduates are not just job-ready, but confident and capable contributors from day one.
