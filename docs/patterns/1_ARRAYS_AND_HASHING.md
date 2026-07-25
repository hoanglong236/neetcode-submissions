# Arrays & Hashing — Pattern Deep Dives

[← Back to Journey Dashboard](../../NEETCODE_250_JOURNEY.md)

---

## I. Bucket Sort

### Core Concept 🌟
**Primary Purpose:** Eliminate comparison overhead in sorting by mapping element values or frequencies directly to array indices, achieving linear time $O(n + k)$ instead of comparison-based $O(n \log n)$.

**Subproblem Signature:** When a larger problem requires sorting or counting data within a **known, bounded range** where the range size is comparable to input size (e.g., counting character frequencies, finding top K elements by frequency, sorting small integer ranges).

**The Mechanism:**
1. Initialize an array of "buckets" with indices corresponding to element values or frequencies.
2. Iterate through input: place each element (or increment its bucket count) at its corresponding index.
3. Reconstruct output by reading buckets sequentially from index 0 onward—data emerges sorted without comparisons.

### Data Triggers & Constraints ⚠️
**Structural Triggers:**
- Bounded value range (e.g., 0–255 for bytes, 0–26 for letters)
- Known maximum frequency or range size
- Array-based indexing is feasible (not sparse data)

**Trade-offs:**
- **Space:** Extra $O(k)$ space for buckets (where $k$ = range size or max frequency) vs. in-place sorting
- **Time:** $O(n + k)$ linear time vs. comparison-based $O(n \log n)$—only beats comparison sort when $k \leq O(n)$
- **Not Adaptive:** Ignores existing order; doesn't benefit from partially sorted data

### Patterns & Problems 🛠️

#### 1. Frequency Array (Fixed-Size Indexing)
*Why this variant:* When counting occurrences of bounded elements (e.g., characters), a fixed array is faster and simpler than a hash map—direct index lookup in $O(1)$ with zero hashing overhead.

- Valid Anagram
- Group Anagrams

#### 2. Top K Frequent (Frequency-Index Inversion)
*Why this variant:* By inverting the mapping—using *frequency as index* instead of value as index—we enable extraction of top K elements in a single $O(n)$ pass without comparison-based sorting.

- Top K Frequent Elements

### Simple Code Implementation

**Frequency Array Pattern** (character counting for anagrams):
```python
def count_char_frequencies(s):
    # Bucket: index = ASCII value, value = frequency
    buckets = [0] * 26  # for a–z lowercase
    for char in s:
        buckets[ord(char) - ord('a')] += 1
    return buckets
```

**Frequency-Index Inversion Pattern** (top K frequent elements):
```python
def bucket_sort_by_frequency(nums):
    # Bucket[i] = list of elements with frequency i
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Read buckets in reverse (highest frequency first)
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        result.extend(buckets[i])
    return result
```

### Key Takeaways 🍀
- **Technique Type:** Index Mapping via Direct Addressing
- **Mental Model:** *"Skip comparisons; use indices instead."* Data structure (array index) replaces sorting logic.
- **Complexity:**
  - Time: $O(n + k)$ (linear traversal + bounded range reconstruction)
  - Space: $O(k)$ (bucket storage for range or frequencies)

---

## II. Prefix / Suffix

### Core Concept 🌟
**Primary Purpose:** Precompute cumulative results (sums, products, counts) at each position to enable answering multiple range-based queries (e.g., "sum between indices L and R") in $O(1)$ constant time, bypassing redundant recalculation.

**Subproblem Signature:** When a problem requires answering **multiple** range-based queries on **static data** (e.g., "sum of elements from index L to R," "product of range"), use precomputed prefix/suffix arrays to service each query in $O(1)$ instead of recalculating from scratch.

**The Mechanism:**
- **1D:** Linear scan computing cumulative result at each index (e.g., running sum): `prefix[i] = prefix[i-1] + arr[i]`
- **2D:** Similar to 1D, scan through the matrix computing cumulative sum at each cell using **Inclusion-Exclusion Principle**: `prefix[i][j] = grid[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]`

### Data Triggers & Constraints ⚠️
**Structural Triggers:**
- Multiple range-based queries on static (immutable) data
- Operations are associative (sum, product, XOR, AND, OR)
- Query frequency justifies $O(n)$ or $O(n \times m)$ preprocessing cost

**Trade-offs:**
- **Space:** Extra $O(n)$ (1D) or $O(n \times m)$ (2D) for prefix arrays vs. querying raw data repeatedly
- **Static Data Limitation:** Highly optimized for **immutable data**; if values change, the entire prefix array must be rebuilt, eliminating the space-time advantage.
- **Associative Operations Only:** Works for sum, product, XOR, AND, OR. **Does NOT work** for min/max (require Segment Trees or Sparse Tables)

### Patterns & Problems 🛠️

#### 1. Linear Accumulation (1D)
Building a running cumulative result by scanning left-to-right or right-to-left through the array.

- Products of Array Except Self
- Trapping Rain Water

#### 2. Grid Accumulation (2D)
Pre-calculating cumulative sums in a matrix to achieve constant-time region sum queries using the **Inclusion-Exclusion Principle**. *(The principle can be applied to other invertible operations like product or XOR)*

- Range Sum Query 2D Immutable

#### 3. Subarray Tracking (Hash Map Extension)
Combining Linear Accumulation with a hash map to track past cumulative states, enabling single-pass detection of target subarrays without precomputing a full prefix array.

- Subarray Sum Equals K
- Subarrays with Given Sum and Bounded Maximum (HackerRank)

*Note: Always initialize the map with `{0: 1}` to represent the empty prefix. This enables detection of subarrays starting at index 0.*

### Simple Code Implementation

**Linear Accumulation Pattern** (1D running sum):
```python
def build_running_sum(nums):
    prefix = []
    cur_sum = 0
    for num in nums:
        cur_sum += num
        prefix.append(cur_sum)
    return prefix
```

**Grid Accumulation Pattern** (2D Inclusion-Exclusion):
```python
def build_matrix_sum_prefix(grid):
    rows, cols = len(grid), len(grid[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

    return prefix
```

### Key Takeaways 🍀
- **Technique Type:** Pre-computation / Space-Time Trade-off
- **Mental Model:** *"Reuse past state."* Store cumulative results to avoid redundant recalculation on overlapping ranges.
- **Complexity:**
  - **Preprocessing (Time & Space):** $O(n)$ (1D) or $O(n \times m)$ (2D) — one-time cost
  - **Per Query (Time):** $O(1)$ after preprocessing

---

## III. Hashing

### Core Concept 🌟
**Instant Retrieval:** Hashing maps data to a unique key using a *Hash Function*. This allows us to store and retrieve data in $O(1)$ average time complexity, regardless of the dataset's size.

### Constraints & Trade-offs ⚠️
- **Memory Overhead:** A classic Space-Time Trade-off. We allocate additional memory to maintain the underlying Hash Table bucket array in exchange for near-instant computational lookups.
- **Unordered Nature:** Standard Hash Maps do not inherently preserve element insertion order.
  *(Note: While Python 3.7+ dictionaries maintain insertion order as an implementation detail, explicitly utilizing collections like `collections.OrderedDict` is safer if order is critical).*

### Patterns & Problems 🛠️

#### 1. Presence Check
Utilizing a Hash Set/Map to check if an element or state has been encountered before.
- Two Sum
- Valid Sudoku
- Longest Consecutive Sequence

#### 2. Frequency Tracking
Utilizing a Hash Map to count occurrences. (Prefer `defaultdict` or `collections.Counter` for convenience)
- Top K Frequent Events with Order Preservation (HackerRank)

#### 3. Index Tracking
Storing the most recent or original index of an element. This is vital for calculating exact spatial distances, valid sliding window boundaries, or identifying unique element spans.
- Top K Frequent Events with Order Preservation (HackerRank)
- Max Unique Substring Length in a Session (HackerRank)

#### 4. Cumulative State Lookup
Mapping previous cumulative running states (sums or products) to find specific target ranges.
- Subarray Sum Equals K
- Subarrays with Given Sum and Bounded Maximum (HackerRank)

### Key Takeaways 🍀
- **Technique Type:** Direct Key-Value Data Mapping.
- **Mental Model:** *Instant Access* — Sacrificing memory to eliminate $O(n)$ search loops.
- **Complexity:**
  - Time: $O(1)$ Average case | $O(n)$ Worst case (under extreme hash collisions)
  - Space: $O(n)$ to store elements within the table

---

## IV. Sorting

### 1. Merge Sort

#### Core Concept 🌟
**Divide and Conquer:** A recursive algorithm that continually splits an array in half until single-element subarrays remain. Since a single element is inherently sorted, the algorithm then builds the solution back up by merging these sorted subarrays in the correct order.

#### The Two Phases ⚔️
- **Divide (Top-Down):** Recursively split the array down the middle, creating a tree of subproblems with a depth of $O(\log n)$ levels.
- **Conquer & Merge (Bottom-Up):** Use a **Two-Pointer approach** to combine two sorted arrays into a single, larger sorted array ($O(n)$ linear work per level).

#### Constraints & Trade-offs ⚠️
- **Space Overhead:** Merge Sort is **not in-place**. It requires $O(n)$ extra memory to hold temporary subarrays during the merge phase.
- **Stability:** It is *a stable sort*, meaning it preserves the original relative order of equal elements. This is highly beneficial when sorting complex objects or multi-key sorting.

#### Patterns & Problems 🛠️

##### 1.1. Divide & Conquer Baseline
We partition a linear structure down the middle, process the independent halves recursively, then build the solution back up.
- Sort an Array (Merge Sort approach)

##### 1.2. Linked List Sorting
Merge Sort is the ideal choice for sorting Linked Lists because they can be easily split in half and merged by simply updating pointer links, requiring $O(1)$ auxiliary space instead of $O(n)$.

#### Key Takeaways 🍀
- **Technique Type:** Recursion / Divide and Conquer.
- **Mental Model:** Split the problem down to its smallest pieces, sort the pieces, and zip them back together.
- **Complexity:**
  - Time: $O(n \log n)$ (Best, Average, and Worst case are identical)
  - Space: $O(n)$ auxiliary memory ($O(1)$ constant overhead for Linked Lists)

---

## V. String Patterns

### Core Concept 🌟
Strings are essentially immutable arrays of characters in Python. While they share sequential data properties with arrays, string-specific problems heavily focus on **serialization** (encoding data into a single stream), **structural formatting** (delimiters, padding, and parsing), and **character transformation** (case manipulation, ASCII math, and reversals).

### Constraints & Trade-offs ⚠️
- **Immutability Overhead:** In Python, modifying a string creates a brand-new copy in memory. Appending characters inside a loop costs $O(n^2)$ time. (Always collect characters in a list `[]` first, then use `"".join(list)` to build the final string in linear $O(n)$ time.)

### Patterns & Problems 🛠️

#### 1. Chunked Transfer Encoding (Length + Delimiter)
When serialization requires separating data safely, use the Length Prefixed Pattern `[Length][Delimiter][Data]` to entirely eliminate delimiter collision bugs.
- Encode and Decode Strings

#### 2. Fixed-Size Frequency Arrays (ASCII Hashing)
Utilize a static array of size 26 or 128 instead of a hash map to track character counts. By mapping characters directly to indices using ASCII math (e.g., `ord(ch) - 65`), you eliminate hash map overhead and unlock raw performance.
- Valid Anagram

---

## VI. Bonus Techniques

### 1. Boyer-Moore Voting Algorithm

#### Core Concept 🌟
An elegant algorithm designed to find the **majority element** (an element that appears more than $\lfloor n/2 \rfloor$ times) in a single pass. It operates on a powerful logic: **canceling out distinct pairs**. If you repeatedly pair up and remove two *different* elements from the array, the element that appears more than half the time is mathematically guaranteed to be the survivor.

#### Patterns & Problems 🛠️

##### 1.1. Single Candidate Tracking
We track a single candidate during a linear scan. The key mechanic is **canceling out distinct pairs**: whenever we encounter an element different from our current candidate, they mutually eliminate each other. When a candidate is completely wiped out by opposites, the next incoming element claims the empty slot.

**Verification Pass:** The ultimate survivor is our answer if a majority is guaranteed; otherwise, a second pass verifies its final count exceeds $\lfloor n/2 \rfloor$.
- Majority Element

##### 1.2. Multiple Candidate Tracking
An advanced extension used to find elements that appear more than $\lfloor n/k \rfloor$ times. We track $k - 1$ candidates. The key mechanic is **canceling out distinct groups of size $k$**: whenever we collect $k$ entirely unique elements, they mutually eliminate each other and free up slots for the next incoming choices.

**Verification Pass:** The ultimate survivors are our answers if $k - 1$ valid majority elements are guaranteed; otherwise, a second pass filters out any false candidates.
- Majority Element II

#### Key Takeaways 🍀
- **Mental Model:** *Cancellation by pairing / multiple grouping*
- **Complexity:** Time: $O(n)$ | Space: $O(1)$

### 2. Greedy (Greedy Strategy)

#### Core Concept 🌟
An algorithmic paradigm that makes the **locally optimal choice** at each step with the intent of finding the globally optimal solution. In array contexts, this typically involves a single linear scan where you capture immediate, guaranteed gains at every local opportunity without considering future trade-offs or looking back at past states.

#### Patterns & Problems 🛠️

##### 2.1. Local Accumulation (Consecutive Delta Scanning)
Instead of searching for a global minimum and maximum across the entire array, we break the problem down into immediate pairs. If the transition from the previous element to the current element yields a positive gain, instantly lock it into the running total.
- Best Time to Buy and Sell Stock II

#### Key Takeaways 🍀
- **Mental Model:** *Grab every immediate profit on the horizon; the future will take care of itself.*
- **Complexity:** Time: $O(n)$ | Space: $O(1)$

### 3. Cyclic Sort

#### Core Concept 🌟
A powerful pattern used when a problem relates to finding missing, duplicate, or misplaced numbers in an array under strict constraints: zero extra memory ($O(1)$ space) and a single pass ($O(n)$ time).

**Home Delivery:** Instead of comparing numbers to see which one is bigger (like traditional sorting), we use the numbers themselves as a map coordinate. Every number $X$ has a "home index" where it belongs (usually index $X - 1$). We walk through the array, and at each step, we find the correct home index for the current element by swapping it with the number currently sitting at its home index. We repeat this swapping process until the current slot holds a number that actually belongs there (or is out of bounds), and only then do we step forward.

#### Constraints & Trade-offs ⚠️
- **In-Place Modification Required:** The $O(1)$ space efficiency relies entirely on mutating the original input array.
- **Partial/Conditional Sorting:** It does not produce a globally sorted array in the traditional sense. Elements that are out of bounds (e.g., negative numbers or numbers larger than the array size) or duplicate values are simply bypassed and left scattered. It only organizes qualifying elements into their precise slots.
- **Unstable Reordering:** Because elements are tossed directly to their target destination index across large gaps, it does not preserve the original relative order of duplicate elements.

#### Patterns & Problems 🛠️

##### 3.1. In-Place Range Mapping (Value to Index Placement)
We use values directly as map coordinates, routing each element to its home index via continuous swapping until the current slot holds a qualifying or out-of-bounds value. After the routing, any index-value pair that fails to match its mapping rule directly exposes a missing or duplicate value.
- First Missing Positive

#### Key Takeaways 🍀
- **Mental Model:** *Home Delivery.*
- **Complexity:**
  - Time: $O(n)$ (Even though there is a nested loop to handle continuous swapping, each element is placed into its correct position at most once, resulting in a maximum of $2n$ total operations.)
  - Space: $O(1)$
