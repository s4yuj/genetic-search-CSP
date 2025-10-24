# variables: [A, B, C, D, E, F, G, H]
# domains: {1, 2, 3, 4}

import numpy as np 

# A, B, C, D, E, F, G, H = [None]*8

def c1(A,B,C,D,E,F,G,H):  return A > G
def c2(A,B,C,D,E,F,G,H):  return A <= H
def c3(A,B,C,D,E,F,G,H):  return abs(F - B) == 1
def c4(A,B,C,D,E,F,G,H):  return G < H
def c5(A,B,C,D,E,F,G,H):  return abs(G - C) == 1
def c6(A,B,C,D,E,F,G,H):  return abs(H - C) % 2 == 0
def c7(A,B,C,D,E,F,G,H):  return D >= G
def c8(A,B,C,D,E,F,G,H):  return D != C
def c9(A,B,C,D,E,F,G,H):  return E != C
def c10(A,B,C,D,E,F,G,H): return E < D - 1
def c11(A,B,C,D,E,F,G,H): return E != H - 2
def c12(A,B,C,D,E,F,G,H): return G != F
def c13(A,B,C,D,E,F,G,H): return H != F
def c14(A,B,C,D,E,F,G,H): return C != F
def c15(A,B,C,D,E,F,G,H): return D != F - 1
def c16(A,B,C,D,E,F,G,H): return abs(E - F) % 2 == 1
def c17(A,B,C,D,E,F,G,H): return H != D

constraints = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17]

DOMAIN = {1,2,3,4}

# each individual is a list of 8 integers
def valid(individual):
    # check individual length
    if len(individual) != 8:
        print("Invalid individual length")
        return False
    
    # check domain validity
    if any(v not in DOMAIN for v in individual):
        print("Invalid individual domain")
        return False
    
    A,B,C,D,E,F,G,H = individual
    return all(c(A,B,C,D,E,F,G,H) for c in constraints)


def fitness(individual):
    A,B,C,D,E,F,G,H = individual
    return sum(c(A,B,C,D,E,F,G,H) for c in constraints)

# reproduce two parents to create two offspring
# crossover point is a random index value between 0 and 7 (inclusive)
# 30% chance of a mutation in each offspring 
def reproduce(parent1, parent2):
    crossover_point1 = np.random.randint(0, 8)  # random point between 0 and 7
    crossover_point2 = np.random.randint(0, 8)  # random point between 0 and 7
    offspring1 = parent1[:crossover_point1] + parent2[crossover_point1:]
    offspring2 = parent2[:crossover_point2] + parent1[crossover_point2:]

    res = (offspring1, offspring2)

    # mutation with 30% chance of changing at most one variable
    for offspring in res:
        if np.random.rand() < 0.3:
            mutate_index = np.random.randint(0, 8)
            # print(f"Mutating offspring {offspring} at index {mutate_index}")
            mutate_value = offspring[mutate_index]
            new_value = np.random.choice(list(DOMAIN - {mutate_value}))
            offspring[mutate_index] = new_value

    # print(f"Parents: {parent1}, {parent2} => Offsprings: {res[0]}, {res[1]}")

    return res

def print_population(population, generation=None):
    if generation is not None:
        print(f"Generation {generation}:")
    for individual in population:
        print(f"Individual: {individual}, Valid: {valid(individual)}, Fitness: {fitness(individual)}")
    print("\n")


def search(population, generations=3):
    for gen in range(generations):

        #check if any individual is a solution already
        for individual in population:
            if valid(individual):
                print(f"Solution found in generation {gen}!")
                print(individual)
                return

        fitness_weights = [fitness(individual) for individual in population]
        total_fitness = sum(fitness_weights)
        selection_probs = [fw / total_fitness for fw in fitness_weights]

        # pick individual indices based on fitness, then grab those rows
        parent_indices = np.random.choice(len(population), size=4, p=selection_probs, replace=False)
        parents = [population[i] for i in parent_indices]

        offspring1, offspring2 = reproduce(parents[0], parents[1])
        offspring3, offspring4 = reproduce(parents[2], parents[3])

        new_population = [offspring1, 
                          offspring2, 
                          offspring3, 
                          offspring4] + sorted(population, key=fitness, reverse=True)[:4]
        population = new_population

        if gen < 3:
            print_population(population, gen + 1)

    print_population(population, generations)

if __name__ == "__main__":
    init_population = [
        [1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2],
        [3,3,3,3,3,3,3,3],
        [4,4,4,4,4,4,4,4],
        [1,2,3,4,1,2,3,4],
        [4,3,2,1,4,3,2,1],
        [1,2,1,2,1,2,1,2],
        [3,4,3,4,3,4,3,4],
    ]

    print_population(init_population, 0)
    search(init_population, generations=1000)