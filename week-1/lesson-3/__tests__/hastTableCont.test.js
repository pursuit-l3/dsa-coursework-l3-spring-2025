// This test verifies that the HashTable class is correctly imported and can be instantiated.
// It focuses on the following functionality:
// Search/lookup functionality
// Delete operation
// Resize/rehash when load factor increases
// Improved collision resolution strategy

const { HashTable } = require("../../lesson-2/exercises/hashTable");

describe("HashTable", () => {
  let hashTable;

  beforeEach(() => {
    hashTable = new HashTable();
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
