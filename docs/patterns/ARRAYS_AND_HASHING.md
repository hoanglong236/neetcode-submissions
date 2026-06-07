# Arrays & Hashing — Pattern Deep Dives

[← Back to Journey Dashboard](../../NEETCODE_250_JOURNEY.md)

---

## I. Bucket Sort

### Core Concept 🌟
**Non-Comparison Sorting:** Unlike standard sorting algorithms that require $O(n \log n)$ time, Bucket Sort can achieve $O(n)$ linear time by completely bypassing comparison logic.

**The Mechanism:** Element values (or their frequencies) are mapped directly to array indices. Because array memory addresses are inherently sequential, the data is structurally "sorted" automatically upon insertion.

### Constraints & Trade-offs ⚠️
- **Value Range:** Only efficient when input values are within a predictable, finite range (e.g., ASCII characters or a fixed range of integers).
- **Space-Time Trade-off:** We use extra space for buckets to avoid the computational cost of sorting.

### Patterns & Problems 🛠️

#### 1. Frequency Array
Utilizing a fixed-size array (e.g., `size=26` for English letters) to count occurrences.
- Valid Anagram
- Group Anagrams

#### 2. Top K Frequent (Frequency-Index Inversion)
Utilizing an array of lists where the *index* of the bucket represents the frequency of the elements.
- Top K Frequent Elements

### Key Takeaways 🍀
- **Technique Type:** Direct Data Mapping (using values/frequencies as indices).
- **Mental Model:** *Address Calculation* — Using indices to avoid sorting.
- **Complexity:**
  - Time: $O(n)$
  - Space: $O(k)$ where $k$ is the bounded range of unique values or maximum frequency.

---

## II. Prefix / Suffix

### Core Concept 🌟
**Pre-computation:** Processing array elements in advance to store partial results (sums, products, or counts). This foundational step allows us to answer range-based queries—finding a result within a specific start and end index $(L, R)$—or lookup past states in $O(1)$ constant time.

### Constraints & Trade-offs ⚠️
- **Space-Time Trade-off:** We allocate extra space to store prefix/suffix results to completely bypass redundant re-computation.
- **Static Data Limitation:** Highly optimized for **immutable data** where values do not change after the prefix array is constructed.

### Patterns & Problems 🛠️

#### 1. Linear Accumulation (1D)
Building a running result by passing through the array linearly (Left-to-Right or Right-to-Left).
- Products of Array Except Self

#### 2. Grid Accumulation (2D)
Pre-calculating areas in a matrix to achieve constant-time region retrievals using the **Inclusion-Exclusion Principle**.
- Range Sum Query 2D Immutable

#### 3. Hash Map + Prefix Sum
Combining current running totals with a "history tracking" hash map of past states to locate specific target subarrays.
- Subarray Sum Equals K
- Subarrays with Given Sum and Bounded Maximum (HackerRank)
  
  *(Always initialize the map with `{0: 1}` to handle subarrays that start at index 0.)*

### Key Takeaways 🍀
- **Technique Type:** Pre-computation / 1D-2D Dynamic Programming.
- **Mental Model:** *Avoid Redundancy* — Reuse the computed result of the immediate previous index or coordinate to evaluate the current state.
- **Complexity:**
  - **1D Accumulation:** Time: $O(n)$ | Space: $O(n)$
  - **2D Grid:** Time: $O(n \times m)$ | Space: $O(n \times m)$

---

## III. Hashing

---

## IV. Sorting

---

## V. String Patterns

---

## VI. Bonus Techniques