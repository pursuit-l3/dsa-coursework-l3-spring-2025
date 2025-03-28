// These tests will check the implementation of the hash table built in the exercises namely:
// Hash function
// Insert operation
// Basic collision handling (linear probing)
//

const { HashTable } = require("../exercises/hashTable");

describe("HashTable", () => {
  let hashTable;

  beforeEach(() => {
    hashTable = new HashTable();
  });

  test("should create a hash table with default size", () => {
    expect(hashTable.size).toBe(8);
    expect(hashTable.count).toBe(0);
  });

  test("should create a hash table with custom size", () => {
    const customHashTable = new HashTable(16);
    expect(customHashTable.size).toBe(16);
    expect(customHashTable.count).toBe(0);
  });

  test("should hash a key to an index", () => {
    const index = hashTable.hash("key");
    expect(index).toBeGreaterThanOrEqual(0);
    expect(index).toBeLessThan(hashTable.size);
  });

  test("should insert a key-value pair", () => {
    const result = hashTable.set("key1", "value1");
    expect(result).toBe(true);
    expect(hashTable.count).toBe(1);
  });

  test("should retrieve a value by key", () => {
    hashTable.set("key2", "value2");
    const value = hashTable.get("key2");
    expect(value).toBe("value2");
  });

  test("should return undefined for non-existent keys", () => {
    const value = hashTable.get("nonExistentKey");
    expect(value).toBeUndefined();
  });

  test("should delete a key-value pair", () => {
    hashTable.set("key3", "value3");
    const result = hashTable.delete("key3");
    expect(result).toBe(true);
    expect(hashTable.count).toBe(0);
  });

  test("should return false when deleting non-existent keys", () => {
    const result = hashTable.delete("nonExistentKey");
    expect(result).toBe(false);
  });
});
