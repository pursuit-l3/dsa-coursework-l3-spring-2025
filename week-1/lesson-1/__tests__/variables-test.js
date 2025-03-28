// days/day1/__tests__/variables.test.js

const {
  demonstrateBlockScope,
  demonstrateConstObjects,
  fixTemporalDeadZone,
  constWithArrays,
} = require("../exercises/variables");

describe("Variables and Scope Exercises", () => {
  test("Exercise 1: demonstrateBlockScope should show different values in different scopes", () => {
    const result = demonstrateBlockScope();
    expect(Array.isArray(result)).toBe(true);
    expect(result.length).toBe(2);
    expect(result[0]).toBe(10); // outer scope value
    expect(result[1]).toBe(20); // inner scope value
  });

  test("Exercise 2: demonstrateConstObjects should show mutable properties", () => {
    const result = demonstrateConstObjects();

    // Original person should have initial values
    expect(result.originalPerson.name).toBe("John");
    expect(result.originalPerson.age).toBe(30);

    // Modified person should have updated values
    expect(result.modifiedPerson.name).toBe("Jane");
    expect(result.modifiedPerson.age).toBe(31);

    // References should be the same
    expect(result.isReferenceEqual).toBe(true);
  });

  test("Exercise 3: fixTemporalDeadZone should return value without error", () => {
    const result = fixTemporalDeadZone();
    expect(result).toBe(10);
  });

  test("Exercise 4: constWithArrays should demonstrate array mutability", () => {
    const result = constWithArrays();
    expect(Array.isArray(result)).toBe(true);
    expect(result.length).toBe(4);
    expect(result).toEqual([1, 2, 3, 4]);
  });
});
