# Google-HashCode-2020
This repository contains solution for the Google HashCode 2020 Qualification Round. This solution has a score of 25,570,294.
The solution leverages priority_queue to avoid O(nlogn) complexity of sorting for both Book and Library classes.

### Solution
The approach adopted for solving the problem is as follows:
1. Each library object have book objects and some attributes describing the library and member functions for submitting books to scan and for computing the metric of each Library
2. The metric for each library is computed as the sum of all book scores in the library divided by the signup_days. Since the metric for a library will be directly proportional to the value of books in the library and inversely proportional to the number of days required to signup the Library
3. After sorting the libraries based of the computed metric, libraries will be picked in descending order of metric
4. After picking a library, books will be scanned according to the score of the book. A book with higher score will be scanned first.

### Some optimization measures:
Some measures were used in coming up with an optimized Solution
1. The attribute that stores the books in a library is a max priority_queue, which allows to pick the book with highest score in O(logn) time instead of O(nlogn)
2. The variable that stores the number of scanned books so far is a set, and this allows for constant lookup time when avoiding duplicate scans for a book
