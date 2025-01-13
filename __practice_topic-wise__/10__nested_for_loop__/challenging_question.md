---

## Challenging

---
Challenging competition-level question emphasize logic building and require advanced use of nested loops for solving real-world scenarios. 
---

### 1. Matrix Border Sum

Given a 2D matrix of size \( n \times n \), calculate the sum of all the elements that lie on the border (outermost layer) of the matrix. Assume the input is always square (equal number of rows and columns).  

#### Input Example:
```plaintext
Matrix:
1 2 3
4 5 6
7 8 9
```
#### Output Example:
```plaintext
Border Sum: 40
```
#### Info:
- Use nested loops to iterate through the rows and columns.
- Sum elements on the first row, last row, first column, and last column while avoiding duplicates.

---

### 2. Knight’s Tour Validation
#### Problem:  
Given a sequence of positions on a chessboard, validate if the sequence represents a valid knight’s tour. The knight can move in an "L" shape: two steps in one direction and one step perpendicular.  
#### Input Example:
```plaintext
Positions: [(0, 0), (2, 1), (0, 2), (1, 4)]
```
#### Output Example:
```plaintext
Valid: False
```
#### Info:
- Use nested loops to validate if the move between each pair of positions follows the knight’s movement rules.
- Track visited positions to ensure no position is revisited.

---

### 3. Triplet Sum Problem
#### Problem:  
Find all unique triplets \((a, b, c)\) in an array such that \( a + b + c = \text{target} \). Each element in the array can only be used once in a triplet.  
#### Input Example:
```plaintext
Array: [1, 2, -3, 4, -1, 0]
Target: 0
```
#### Output Example:
```plaintext
Triplets: [(1, -1, 0), (2, -3, 1)]
```
#### Info:
- Use three nested loops to try all combinations of triplets.
- Avoid duplicate triplets by sorting or using a set to store results.

---

### 4. Matrix Spiral Traversal
#### Problem:  
Traverse a given \( m \times n \) matrix in spiral order (starting from the top-left corner and going clockwise).  
#### Input Example:
```plaintext
Matrix:
1  2  3
4  5  6
7  8  9
```
#### Output Example:
```plaintext
Spiral Order: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
#### Info:
- Use nested loops to traverse the outer layer, then move inward layer by layer.
- Handle edge cases like a single row or column.

---

### 5. Magic Square Validation
#### Problem:  
Given a \( n \times n \) 2D matrix, check if it forms a magic square. A magic square has equal sums for all rows, columns, and diagonals.  
#### Input Example:
```plaintext
Matrix:
8 1 6
3 5 7
4 9 2
```
#### Output Example:
```plaintext
Is Magic Square: True
```
#### Info:
- Use nested loops to calculate the sum of rows, columns, and diagonals.
- Compare all sums to the first row’s sum to validate.

---

### 6. Word Search in a Grid
#### Problem:  
Given a 2D grid of characters and a target word, check if the word exists in the grid. The word can be formed by adjacent letters horizontally, vertically, or diagonally, but cannot reuse the same cell twice.  
#### Input Example:
```plaintext
Grid:
A B C E
S F C S
A D E E
Word: "ABCCED"
```
#### Output Example:
```plaintext
Exists: True
```
#### Info:
- Use nested loops to find the starting letter.
- Perform a recursive or nested search from the starting position.

---

### 7. Largest Rectangle in a Histogram
#### Problem:  
Given an array representing bar heights in a histogram, find the largest rectangular area under the histogram.  
#### Input Example:
```plaintext
Heights: [2, 1, 5, 6, 2, 3]
```
#### Output Example:
```plaintext
Largest Area: 10
```
#### Info:
- Use nested loops to calculate areas for all possible rectangles.
- For each bar, expand left and right to find the largest rectangle.

---

### 8. Count Distinct Islands
#### Problem:  
Given a 2D grid representing land (`1`) and water (`0`), count the number of distinct islands. Two islands are distinct if their shapes differ.  
#### Input Example:
```plaintext
Grid:
1 1 0 0
1 0 0 1
0 0 1 1
```
#### Output Example:
```plaintext
Distinct Islands: 2
```
#### Info:
- Use nested loops to iterate through the grid.
- Use DFS/BFS to explore each island and track its shape relative to the starting point.

---

### 9. Sudoku Solver
#### Problem:  
Solve a partially filled Sudoku grid using nested loops. A Sudoku grid is valid if every row, column, and 3x3 subgrid contains unique numbers from 1 to 9.  
#### Input Example:
```plaintext
Grid:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
```
#### Output Example:
```plaintext
Solved Sudoku:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
```
#### Info:
- Use nested loops to fill empty cells.
- Check row, column, and subgrid constraints for each cell.

---

### 10. Minimum Knight Moves
#### Problem:  
Given a starting position and a target position on a chessboard, calculate the minimum number of moves required for a knight to reach the target.  
#### Input Example:
```plaintext
Start: (0, 0)
Target: (7, 7)
```
#### Output Example:
```plaintext
Minimum Moves: 6
```
#### Info:
- Use nested loops to simulate all possible moves from each position.
- Use BFS to track visited positions and find the shortest path.

---
