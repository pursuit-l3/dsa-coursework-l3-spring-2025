// days/day1/exercises/variables.js

/**
 * Exercise 1: Block Scope with let
 *
 * Complete the function to demonstrate block scope using 'let'.
 * The function should:
 * 1. Declare a variable 'x' with value 10 in the outer scope
 * 2. Create a block that declares the same variable 'x' with value 20
 * 3. Return an array containing both values of x [outerX, innerX]
 */
function demonstrateBlockScope() {
  // Your code here
}

/**
 * Exercise 2: Constants
 *
 * Implement a function that shows the difference between:
 * - A constant primitive value (can't be changed)
 * - A constant object reference (properties can be modified)
 *
 * Return an object with properties:
 * - originalPerson: The initial person object
 * - modifiedPerson: The person object after modifications
 * - isReferenceEqual: Boolean indicating if both references are the same
 */
function demonstrateConstObjects() {
  // Your code here
}

/**
 * Exercise 3: Temporal Dead Zone
 *
 * Rewrite the function to use let/const properly and avoid the temporal dead zone issue.
 * The function should now run without errors and return the value of 'x'.
 */
function fixTemporalDeadZone() {
  // The original problematic code:
  // console.log(x);  // ReferenceError
  // let x = 10;
  // Your fixed code here
}

/**
 * Exercise 4: Const for Arrays
 *
 * Implement a function that:
 * 1. Declares an array as a constant
 * 2. Adds items to the array (which works despite it being a constant)
 * 3. Try to reassign the array (should fail)
 * 4. Return the modified array
 */
function constWithArrays() {
  // Your code here
}

module.exports = {
  demonstrateBlockScope,
  demonstrateConstObjects,
  fixTemporalDeadZone,
  constWithArrays,
};
