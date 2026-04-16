# AI Lab - Complete Guide & Explanations 🤖

---

## **OVERVIEW**
This document provides detailed explanations of all the AI Lab assignments (Week 01 to Week 09). Each lab covers different topics in Artificial Intelligence including data manipulation, search algorithms, game playing, and machine learning.

---

## **TABLE OF CONTENTS**
1. [Week 01 - Python Basics](#week-01---python-basics)
2. [Week 02 - Python Data Structures](#week-02---python-data-structures)
3. [Week 03 - NumPy Arrays](#week-03---numpy-arrays)
4. [Week 04 - Data Analysis](#week-04---data-analysis)
5. [Week 05 - Advanced Data Analysis](#week-05---advanced-data-analysis)
6. [Week 06 - A* Search Algorithm](#week-06---a-search-algorithm)
7. [Week 07 - Tic Tac Toe with Minimax](#week-07---tic-tac-toe-with-minimax)
8. [Week 08 - More Advanced Topics](#week-08---more-advanced-topics)
9. [Week 09 - K-Nearest Neighbors (KNN)](#week-09---k-nearest-neighbors-knn)

---

## **WEEK 01 - Python Basics**

### **File:** `Week_01/abubakar_54603.ipynb`

### **Topics Covered:**
- Python fundamentals
- Basic data types (int, float, string, boolean)
- Variables and operators
- Control flow (if-else, loops)
- Functions

### **What You'll Learn:**
- How to write and execute basic Python code
- Understanding of Python syntax and structure
- Problem-solving with simple logic

### **Key Concepts:**
- **Variables**: Store data in memory
- **Data Types**: Different types of data (numbers, text, etc.)
- **Operators**: Mathematical, logical, and comparison operations
- **Control Flow**: Making decisions and repeating tasks

---

## **WEEK 02 - Python Data Structures**

### **File:** `Week_02/abubakar_54603.ipynb`

### **Topics Covered:**
- Lists (arrays)
- Tuples (immutable sequences)
- Dictionaries (key-value pairs)
- Sets (unique collections)
- List comprehensions

### **What You'll Learn:**
- How to create and manipulate different data structures
- When to use each data structure
- Efficient ways to access and modify data

### **Key Concepts:**
- **Lists**: Ordered, mutable collection `[1, 2, 3]`
- **Tuples**: Ordered, immutable collection `(1, 2, 3)`
- **Dictionaries**: Key-value pairs `{"name": "Ali", "age": 20}`
- **Sets**: Unique elements `{1, 2, 3}`
- **List Comprehensions**: Compact way to create lists `[x*2 for x in range(5)]`

---

## **WEEK 03 - NumPy Arrays**

### **File:** `Week_03/Week03_Lab03.ipynb`

### **Topics Covered:**
1. **Importing NumPy** - Installing and using the NumPy library
2. **Array Creation** - Creating arrays from lists
3. **Array Dimensions** - 1D, 2D, 3D, 4D, 5D arrays
4. **Array Operations** - Basic mathematical operations
5. **Array Slicing** - Extracting parts of arrays
6. **Data Types** - Different data types in arrays (int, float, complex, etc.)
7. **Array Reshaping** - Changing array dimensions
8. **Array Copy vs View** - Understanding memory management
9. **Array Iteration** - Looping through arrays
10. **Other Operations** - Joining, splitting, searching, sorting arrays

### **Detailed Explanations:**

#### **1. Array Creation**
```python
import numpy as np

# 1D Array
arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim)  # Output: 1

# 2D Array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.ndim)  # Output: 2

# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d.ndim)  # Output: 3
```

**Key Points:**
- `ndim`: Number of dimensions
- `shape`: Size of array in each dimension
- `dtype`: Data type of elements

#### **2. Array Slicing**
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

arr[1:5]      # Output: [2, 3, 4, 5] (from index 1 to 4)
arr[::2]      # Output: [1, 3, 5, 7] (every 2nd element)
arr[::-1]     # Output: [7, 6, 5, 4, 3, 2, 1] (reversed)
```

#### **3. Data Types**
- `int64`: Integer (default for whole numbers)
- `float64`: Float (default for decimals)
- `complex128`: Complex numbers
- `bool`: Boolean (True/False)
- `object`: Any Python object

#### **4. Reshaping**
```python
arr = np.arange(12)  # [0, 1, 2, ..., 11]
reshaped = arr.reshape(3, 4)  # Convert to 3x4 matrix

# Shape: (3, 4)
# [[0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9, 10, 11]]
```

#### **5. Operations**
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise operations
arr1 + arr2       # [5, 7, 9]
arr1 * arr2       # [4, 10, 18]
np.concatenate([arr1, arr2])  # [1, 2, 3, 4, 5, 6]
np.array_split(arr1, 3)  # Split into 3 parts
```

### **Task:** Create a 3x3 matrix with values 2-10, reshape it, convert to float, and find max/min

---

## **WEEK 04 - Data Analysis**

### **File:** `Week_04/Week04_Lab04.ipynb`

### **Topics Covered:**
- Pandas DataFrames and Series
- Loading data from files
- Data exploration and statistics
- Data cleaning and preprocessing
- Visualization with matplotlib

### **What You'll Learn:**
- How to work with real-world datasets
- Finding patterns in data
- Handling missing values
- Creating visualizations

### **Key Concepts:**
- **DataFrame**: 2D table with rows and columns
- **Series**: 1D labeled array
- **Aggregation**: Summarizing data (sum, mean, count)
- **Grouping**: Organizing data by categories
- **Filtering**: Selecting specific rows

---

## **WEEK 05 - Advanced Data Analysis**

### **File:** `Week_05/Week05_Lab05.ipynb`

### **Topics Covered:**
- Advanced pandas operations
- Merging and joining datasets
- Time series analysis
- Statistical analysis
- More complex visualizations

### **What You'll Learn:**
- How to combine multiple datasets
- Working with temporal data
- Statistical significance testing
- Creating publication-quality plots

---

## **WEEK 06 - A* SEARCH ALGORITHM** ⭐

### **File:** `Week_06/Week06_Lab06.ipynb`

### **What is A* Search?**

A* is an **intelligent graph search algorithm** that combines:
- **g(n)**: Cost from start to current node
- **h(n)**: Estimated cost from current to goal (heuristic)
- **f(n) = g(n) + h(n)**: Total estimated cost

### **Why A* is Better Than Other Algorithms:**
- **Breadth-First Search (BFS)**: Explores all nodes at distance d before distance d+1 (wastes time)
- **Depth-First Search (DFS)**: Can get stuck in wrong direction
- **A***: Uses heuristic to guide search toward goal (smarter!)

### **How A* Works (Step by Step):**

1. **Initialize**: Create open list with start node
2. **Loop until goal found**:
   - Pick node with lowest f(n) from open list
   - If it's the goal, we're done!
   - Expand it: generate all neighbors
   - For each neighbor:
     - Calculate g(n) = cost from start
     - Calculate h(n) = estimated cost to goal
     - Calculate f(n) = g(n) + h(n)
     - Add to open list if not visited

### **Example 1: 8-Puzzle Solver**

**Problem**: Rearrange tiles to match goal state

```
Initial State:          Goal State:
2 8 3                   1 2 3
1 6 4          →        8 0 4
7 0 5                   7 6 5
```

**How it works:**
- **Heuristic**: Count misplaced tiles (Manhattan distance)
- **Cost g(n)**: Number of moves made
- **Priority**: Nodes with lowest f(n) are explored first
- **Result**: Finds shortest path in 7 moves

### **Example 2: Graph Path Finding**

```
Graph:
A -1- B -3- D
|     |
4     2
|     |
C -5- F -1- E

Goal: Find shortest path from A to F
```

**A* solves it by**:
- Trying paths intelligently based on distance estimate
- Skipping obvious bad choices
- Finding optimal path: A → B → E → F (cost = 4)

### **Key Insights:**
- **Admissible Heuristic**: h(n) never overestimates (guarantees optimal solution)
- **Consistency**: If h never decreases too quickly along a path
- **Efficiency**: Far fewer nodes explored than uninformed search

---

## **WEEK 07 - TIC TAC TOE WITH MINIMAX** 🎮

### **Files:**
- `Week_07/TicTacToe/CLI/TicTacToe_CLI.py` (Command Line Version)
- `Week_07/TicTacToe/GUI/TicTacToe_GUI.py` (Graphical Version)

### **What is Minimax Algorithm?**

Minimax is a **game-playing algorithm** that finds the best move in a two-player game by:
1. Assuming both players play optimally
2. Exploring all possible future game states
3. Scoring states (win/loss/draw)
4. Working backward to find best current move

### **Key Concept: Maximizer vs Minimizer**

```
         Maximizer (X) ← Wants HIGH score (10)
         /
      Game Tree
        /
   Minimizer (O) ← Wants LOW score (-10)
```

- **Maximizer (You/X)**: Tries to get highest score (+10 if X wins)
- **Minimizer (AI/O)**: Tries to get lowest score (-10 if O wins)

### **How Minimax Works for Tic Tac Toe:**

1. **Evaluation Function**:
   - +10 if X wins
   - -10 if O wins
   - 0 if draw

2. **Minimax Process**:
   ```
   Function minimax(depth, is_maximizing):
       if game_over:
           return score
       
       if is_maximizing:
           best = -infinity
           for each empty cell:
               try move
               best = max(best, minimax(depth+1, False))
               undo move
           return best
       else:
           best = +infinity
           for each empty cell:
               try move
               best = min(best, minimax(depth+1, True))
               undo move
           return best
   ```

3. **Finding Best Move for AI**:
   - Try each empty position
   - Run minimax to see outcome
   - Pick move with LOWEST score (O wants to minimize)
   - Result: Unbeatable AI!

### **Why AI Plays Perfectly:**

1. Explores ALL possible future states
2. Evaluates each outcome (-10, 0, or 10)
3. Chooses move that leads to best outcome
4. Since AI minimizes and human maximizes, they find optimal play
5. Against perfect play: Result is always a DRAW

### **Game Flow:**
```
1. Human (X) makes move
2. Check if game over
3. AI (O) uses minimax to find best move
4. Repeat until win/loss/draw
```

### **Code Explanation:**

**Print Board:**
- Displays 3x3 grid with row/column numbers
- Shows '_' for empty, 'x' for human, 'o' for AI

**Evaluate:**
- Checks all 3 rows for winner
- Checks all 3 columns for winner
- Checks both diagonals for winner

**Minimax:**
- Recursive function exploring all possibilities
- Returns score at leaf nodes
- Backtracks to find best move

**Best Move:**
- Tries each empty cell
- Gets minimax score for that move
- Picks cell with minimum score (AI perspective)

---

## **WEEK 08 - Advanced Topics**

### **File:** `Week_08/Week08_Lab08.ipynb`

### **Topics Covered:**
- More complex algorithms
- Performance optimization
- Advanced data structures

### **What You'll Learn:**
- How to solve complex problems
- Optimizing code for speed
- Working with specialized data structures

---

## **WEEK 09 - K-NEAREST NEIGHBORS (KNN)** 📊

### **File:** `Week_09/KNN_Lab09.ipynb`

### **What is KNN?**

KNN is a **simple but powerful machine learning algorithm** for **classification and regression**.

**Main Idea**: "You are the average of your 5 closest friends"

### **How KNN Works:**

1. **Store Training Data**: Remember all training examples
2. **Calculate Distances**: When classifying new point, find distance to all training points
3. **Find K Neighbors**: Pick the K nearest points
4. **Vote**: Most common label among K neighbors becomes the prediction

### **Distance Metrics:**

**Euclidean Distance** (most common):
```
distance = sqrt((x1-x2)² + (y1-y2)²)
```

Example in 2D:
```python
point1 = (2, 3)
point2 = (5, 7)
distance = sqrt((5-2)² + (7-3)²) = sqrt(9+16) = 5
```

### **Algorithm Steps:**

```
KNN Classification(new_point, K):
    distances = []
    
    for each training_point in dataset:
        distance = euclidean_distance(new_point, training_point)
        distances.append((distance, label))
    
    # Sort by distance, get K nearest
    k_nearest = sorted(distances)[:K]
    
    # Vote: most common label
    labels = [label for _, label in k_nearest]
    prediction = most_common_label(labels)
    
    return prediction
```

### **Example: Classifying Iris Flowers**

```
Dataset: 150 iris flowers with 4 features each
Features: Sepal length, Sepal width, Petal length, Petal width
Classes: Setosa, Versicolor, Virginica

New flower: (5.1, 3.5, 1.4, 0.2)
K = 3

Distances to all flowers:
    Flower 1 (Setosa): 0.15
    Flower 2 (Setosa): 0.22
    Flower 3 (Setosa): 0.30    ← 3 nearest
    Flower 4 (Versicolor): 2.5
    ...

3 Nearest neighbors: Setosa, Setosa, Setosa
Prediction: SETOSA ✓
```

### **Choosing K:**

- **K=1**: Fast, but noisy (sensitive to outliers)
- **K=3-5**: Good balance (most common)
- **K=10**: Smoother decisions, slower
- **K too high**: Loses local patterns

**Rule of thumb**: K = sqrt(n) where n = number of training samples

### **Advantages:**
✓ Simple to understand
✓ No training phase (lazy learner)
✓ Works for both classification and regression
✓ Can adapt to any feature space

### **Disadvantages:**
✗ Slow for large datasets (must check all points)
✗ Memory intensive (stores all training data)
✗ Sensitive to irrelevant features
✗ Needs feature scaling (distances affected by scale)

### **Implementation Tips:**

1. **Normalize Features**: Scale all features to 0-1 range
   ```python
   normalized = (x - min) / (max - min)
   ```

2. **Feature Scaling**: Prevents large features from dominating
   ```python
   # Without scaling: feature A ranges 0-1000, feature B ranges 0-1
   # With scaling: both range 0-1
   ```

3. **Cross-Validation**: Test with different K values
   ```python
   for K in [1, 3, 5, 7, 9]:
       accuracy = test_KNN(K)
       print(f"K={K}: {accuracy}%")
   ```

### **KNN vs Other Algorithms:**

| Algorithm | Training | Prediction | Memory | Accuracy |
|-----------|----------|-----------|--------|----------|
| KNN | Fast | Slow | High | Good |
| Decision Tree | Slow | Fast | Low | Good |
| Neural Network | Very Slow | Fast | High | Very Good |
| Logistic Regression | Medium | Fast | Low | Good |

### **Real-World Applications:**

1. **Recommendation Systems**: Netflix, Spotify recommend based on similar users
2. **Image Classification**: Finding similar images
3. **Medical Diagnosis**: Finding similar patient cases
4. **Credit Scoring**: Finding similar loan applicants
5. **Handwriting Recognition**: Matching similar digit patterns

### **Implementation Example:**

```python
from sklearn.neighbors import KNeighborsClassifier

# Create classifier with K=3
knn = KNeighborsClassifier(n_neighbors=3)

# Training
knn.fit(X_train, y_train)

# Prediction
predictions = knn.predict(X_test)

# Accuracy
accuracy = knn.score(X_test, y_test)
print(f"Accuracy: {accuracy*100}%")
```

---

## **GENERAL AI CONCEPTS SUMMARY**

### **1. Search Algorithms Hierarchy**

```
Search Algorithms
├── Uninformed (Blind)
│   ├── Breadth-First Search (BFS)
│   ├── Depth-First Search (DFS)
│   └── Iterative Deepening
│
├── Informed (Heuristic)
│   ├── Greedy Best-First
│   ├── A* Search ⭐
│   └── Bidirectional Search
│
└── Adversarial (Game Playing)
    ├── Minimax ⭐
    ├── Alpha-Beta Pruning
    └── Monte Carlo Tree Search
```

### **2. Learning Algorithms Hierarchy**

```
Machine Learning
├── Supervised Learning
│   ├── Classification
│   │   ├── K-Nearest Neighbors ⭐
│   │   ├── Decision Trees
│   │   ├── Neural Networks
│   │   └── SVM
│   │
│   └── Regression
│       ├── Linear Regression
│       └── Polynomial Regression
│
├── Unsupervised Learning
│   ├── Clustering (K-Means)
│   └── Dimensionality Reduction (PCA)
│
└── Reinforcement Learning
    ├── Q-Learning
    └── Deep RL
```

### **3. Key AI Problem-Solving Approaches**

1. **Search Problems**: Find path from start to goal
   - Uses: A*, Minimax, BFS/DFS
   - Examples: Navigation, Game Playing

2. **Optimization Problems**: Find best solution
   - Uses: Gradient Descent, Genetic Algorithms
   - Examples: Training Neural Networks

3. **Classification Problems**: Assign to category
   - Uses: KNN, Decision Trees, Neural Networks
   - Examples: Email spam detection, Image recognition

4. **Prediction Problems**: Forecast future values
   - Uses: Linear/Polynomial Regression, ARIMA
   - Examples: Stock prices, Weather forecasting

---

## **HANDS-ON EXERCISES**

### **Exercise 1: NumPy Practice**
Create a 5x5 matrix with random numbers, find sum, mean, max, min, and standard deviation.

### **Exercise 2: A* Challenge**
Modify the 8-puzzle solver to handle different goal states, or implement A* for maze solving.

### **Exercise 3: Minimax Extended**
Add alpha-beta pruning to Tic Tac Toe for better performance, or implement Connect 4.

### **Exercise 4: KNN Variations**
Test KNN with different K values on the Iris dataset and create a plot showing accuracy vs K.

### **Exercise 5: Comparison Project**
Compare A*, Minimax, and BFS on the same problem (e.g., puzzle solving) in terms of:
- Number of nodes explored
- Time taken
- Solution quality

---

## **COMMON MISTAKES TO AVOID**

1. **NumPy**: Confusing views vs copies (modifications affect originals)
2. **A***: Using non-admissible heuristic (might not find optimal solution)
3. **Minimax**: Not handling terminal states properly
4. **KNN**: Not normalizing features (large scales dominate)
5. **Data Analysis**: Not checking for missing values or outliers

---

## **KEY TAKEAWAYS**

| Week | Topic | Key Concept | Application |
|------|-------|------------|------------|
| 01-02 | Python Basics | Programming fundamentals | Foundation for all coding |
| 03-05 | Data Processing | Arrays and DataFrames | Handling data efficiently |
| 06 | A* Search | Heuristic search | Navigation, Pathfinding |
| 07 | Minimax | Game AI | Perfect play strategies |
| 08 | Advanced | Complex algorithms | Real-world problems |
| 09 | KNN | Classification | Machine Learning basics |

---

## **RESOURCES FOR FURTHER LEARNING**

1. **NumPy Documentation**: https://numpy.org/doc/
2. **Pandas Guide**: https://pandas.pydata.org/docs/
3. **A* Algorithm**: https://en.wikipedia.org/wiki/A*_search_algorithm
4. **Minimax**: https://en.wikipedia.org/wiki/Minimax
5. **KNN**: https://scikit-learn.org/stable/modules/neighbors.html

---

## **CONCLUSION**

This AI Lab course covers:
- **Data Fundamentals**: NumPy, Pandas, arrays
- **Search & Problem Solving**: A*, Minimax, graph algorithms
- **Game AI**: Optimal strategies for two-player games
- **Machine Learning**: Classification with KNN

Each topic builds upon previous concepts, creating a comprehensive foundation in AI and machine learning!

---

**Happy Learning! 🚀**

*Last Updated: April 2026*
*Created by: Your Name | SAP ID: 54603*

