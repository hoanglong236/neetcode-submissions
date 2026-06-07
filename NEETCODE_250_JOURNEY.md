# 🚀 My NeetCode 250 Engineering Journey

Welcome to my personal roadmap for mastering Data Structures and Algorithms. While this repository automatically backs up my raw code submissions, this dashboard serves as my engineering log—tracking concept mastery, pattern recognition, and architectural insights.

---

## 📊 Progress Dashboard

| Category | Progress | Status |
| :--- | :--- | :--- |
| **Arrays & Hashing** | 20 / 22 | 🔄 Near Completion |
| **Two Pointers** | 12 / 13 | 🔄 Near Completion |
| **Sliding Window** | 1 / 9  | ⏳ Pending |

> **Total Progress:** `33 / 250` Problems Mastered

---

## 🛡️ Pattern Archives & Concept Documentation

### ⏱️ Foundational Baseline: Big-O Notation

Before diving into specific patterns, we establish our core language for efficiency evaluation. Big-O notation is a mathematical framework used to measure an algorithm's structural efficiency. It describes how runtime (**Time Complexity**) or memory footprint (**Space Complexity**) scales relative to the input size $(n)$, focusing strictly on the theoretical *worst-case scenario* to guarantee absolute performance boundaries.

| Complexity | Official Name | Growth Rate & Behavior | Efficiency Rating | Typical Example |
| :--- | :--- | :--- | :--- | :--- |
| $O(1)$ | **Constant** | Growth is completely flat. Speed is completely independent of input size $n$. | 🟢 Excellent | Array index lookup, Hash map insertion |
| $O(\log n)$ | **Logarithmic** | Growth curves flat. Execution steps are halved at every iteration. | 🟢 Excellent | Binary Search |
| $O(n)$ | **Linear** | Growth scales 1:1 directly proportional to the input size $n$. | 🟡 Fair | Single loop pass, Bucket sort mapping |
| $O(n \log n)$ | **Linearithmic** | Growth is slightly worse than linear. Standard for optimal sorting. | 🟡 Fair | Merge Sort, Quick Sort, Heap Sort |
| $O(n^2)$ | **Quadratic** | Growth scales exponentially. Performance degrades rapidly on large $n$. | 🔴 Horrible | Nested loops (e.g., Bubble Sort, Brute Force) |
| $O(2^n)$ | **Exponential** | Growth doubles with each addition to $n$. Severely limits max input size. | 🔴 Horrible | Recursive Fibonacci, generating subsets |
| $O(n!)$ | **Factorial** | Growth explodes instantly. Virtually unusable for inputs greater than $n \approx 12$. | ☠️ Catastrophic | Generating all possible permutations |


### 🗂️ Knowledge Base Directory

To maintain a clean and scalable dashboard, detailed algorithmic breakdowns are organized into modular documentation files by topic.

* **[Arrays & Hashing Documentation](./docs/patterns/1_ARRAYS_AND_HASHING.md)**
    * *Featured Patterns:* Bucket Sort, Frequency Mapping, Prefix Sums, Hash Multi-sets.
    * *Status:* 🟢 Documentation In Progress
* **[Two Pointers Documentation](./docs/patterns/2_TWO_POINTERS.md)**
    * *Featured Patterns:* Extreme Boundaries, Segment Reversal, Slow/Fast Pointers.
    * *Status:* 🟢 Documentation In Progress
* **[Sliding Window Documentation](./docs/patterns/3_SLIDING_WINDOW.md)**
    * *Featured Patterns:* Fixed vs. Dynamic Windows, Counter-Driven Frequency Validation.
    * *Status:* ⏳ Pending Implementation

---
*Last updated: June 2026*