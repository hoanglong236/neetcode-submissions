# Arrays & Hashing — Pattern Deep Dives

[← Back to Journey Dashboard](../../NEETCODE_250_JOURNEY.md)

---

## I. Bucket Sort

### 🌟 Core Concept
**Non-Comparison Sorting:** Unlike standard sorting algorithms that require $O(n \log n)$ time, Bucket Sort can achieve $O(n)$ linear time by completely bypassing comparison logic.

**The Mechanism:** Element values (or their frequencies) are mapped directly to array indices. Because array memory addresses are inherently sequential, the data is structurally "sorted" automatically upon insertion.

### ⚠️ Constraints & Trade-offs
- **Value Range:** Only efficient when input values are within a predictable, finite range (e.g., ASCII characters or a fixed range of integers).
- **Space-Time Trade-off:** We use extra space for buckets to avoid the computational cost of sorting.

### 🛠️ Patterns & Problems
#### 1. Frequency Array
Utilizing a fixed-size array (e.g., `size=26` for English letters) to count occurrences.
- Valid Anagram
- Group Anagrams

#### 2. Top K Frequent (Frequency-Index Inversion)
Utilizing an array of lists where the *index* of the bucket represents the frequency of the elements.
- Top K Frequent Elements

### 🍀 Key Takeaways
- **Technique Type:** Direct Data Mapping (using values/frequencies as indices).
- **Mental Model:** *Address Calculation* — Using indices to avoid sorting.
- **Complexity Analysis:**
  - **Time:** $O(n)$
  - **Space:** $O(k)$ where $k$ is the bounded range of unique values or maximum frequency.

---

## II. Prefix / Suffix

---

## III. Hashing

---

## IV. Sorting

---

## V. String Patterns

---

## VI. Bonus Techniques