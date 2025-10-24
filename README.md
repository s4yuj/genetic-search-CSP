# Genetic Search for Constraint Satisfaction Problems (CSP)

## Overview
This project implements a **Genetic Algorithm (GA)** with **Stochastic Local Search (SLS)** to efficiently find valid or near-valid solutions to **Constraint Satisfaction Problems (CSPs)**.  

Instead of exploring the entire search space exhaustively, the algorithm evolves a population of candidate solutions toward higher constraint satisfaction using **selection**, **crossover**, and **mutation**.

---

## Algorithm Summary

1. **Initialize Population:**  
   Start with random candidate solutions. Fitness = number of constraints satisfied.

2. **Evaluate Fitness:**  
   Compute each individual’s fitness and normalize to probabilities.

3. **Selection:**  
   Randomly pick 4 individuals using weighted probabilities (`numpy.random.choice`).

4. **Crossover:**  
   - Two random crossover points (`numpy.random.randint(0,7)`)  
   - Create offspring by combining halves of two parents.

5. **Mutation:**  
   Each offspring has a **30% chance** to mutate (`numpy.random.rand() < 0.3`).

6. **Next Generation:**  
   Combine **4 offspring** + **4 fittest members** (elitism).  
   Repeat for a fixed number of generations (default = 3) or until a valid solution is found.

---

## Runtime analysis?

Traditional CSP solvers have **exponential complexity** —  
> **O(kⁿ)**, where `k` = domain size and `n` = number of variables.  

This algorithm avoids full enumeration by sampling and evolving a limited population:

| Complexity | Full Search | GA–SLS |
|-------------|-------------|--------|
| **Time** | O(kⁿ) | O(g × p × f) |
| **Space** | O(kⁿ) | O(p) |

where:  
- `g` = generations  
- `p` = population size  
- `f` = fitness evaluation cost  

**Result:** Dramatic reduction in time and memory — from exponential to roughly polynomial.
