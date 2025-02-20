# Knapsack Solver Using DFS and a Genetic Algorithm

This project demonstrates two methods to solve the 0/1 knapsack problem in Python:

1. **Depth-First Search (DFS)** – an exhaustive search guaranteeing the optimal solution.
2. **Genetic Algorithm (GA)** – a heuristic approach inspired by natural evolution to find high-quality solutions efficiently.

The evaluation module compares both methods and visualizes their performance.

---

## Table of Contents

- [Overview](#overview)
- [Files](#files)
- [How It Works](#how-it-works)
  - [DFS](#dfs-depth-first-search)
  - [Genetic Algorithm](#genetic-algorithm)
  - [Evaluation](#evaluation)
- [Installation](#installation)
- [Usage](#usage)
- [Customization & Parameters](#customization--parameters)
- [Example](#example)
- [Notes](#notes)

---

## Overview

The knapsack problem involves selecting items with maximum total value without exceeding a weight capacity.

- **DFS** explores all possible item combinations (optimal but computationally expensive).
- **GA** evolves solutions over generations using selection, crossover, mutation, and elitism (faster for large datasets but heuristic).

---

## Files

| File            | Description                                                                        |
| --------------- | ---------------------------------------------------------------------------------- |
| `DFS.py`        | Implements DFS with stack-based backtracking to find the optimal solution.         |
| `GA.py`         | Genetic Algorithm with adaptive mutation, elitism, and multiple crossover methods. |
| `Evaluation.py` | Compares DFS and GA results and generates plots using `matplotlib`.                |
| `main.py`       | Entry point: loads data, initializes solvers, and runs evaluation.                 |

---

## How It Works

### DFS (Depth-First Search)

- **Key Methods**:
  - `run()`: Uses a stack to explore all item subsets.
  - `calculate_weight_value()`: Computes weight and value for a solution.
- **Guarantees optimality** but may be slow for >20 items due to exponential complexity.

### Genetic Algorithm

- **Key Features**:
  - **Adaptive Mutation**: Increases mutation rate if population diversity drops below 20%.
  - **Elitism**: Preserves top 10% of solutions across generations.
  - **Selection Methods**: Tournament or roulette wheel.
  - **Crossover Methods**: One-point or uniform.
- **Fitness Calculation**: Penalizes overweight solutions.
- **Diversity Check**: Stops early if population becomes too homogeneous.

### Evaluation

- `compare_solvers()`: Runs DFS and GA on problem instances.
- `plot_results()`: Generates bar charts comparing solution values.

---

## Installation

1. **Dependencies**:
   ```bash
   pip install matplotlib
   ```
