import random

class GeneticAlgorithm:
    def __init__(self, items, capacity, population_size=20, generations=100, mutation_rate=0.05, 
                 crossover_rate=0.8, elitism=True, selection_method="tournament", 
                 diversity_threshold=0.05, crossover_method="one_point_crossover"):
        """
        Initialize the Genetic Algorithm solver.

        :param items: List of items (each item is a dict with "weight" and "value").
        :param capacity: Maximum weight capacity of the knapsack.
        :param population_size: Number of individuals in the population.
        :param generations: Number of generations to run the algorithm.
        :param mutation_rate: Probability of mutation.
        :param crossover_rate: Probability of crossover.
        :param elitism: Whether to preserve the best individuals.
        :param selection_method: Selection strategy ("tournament" or "roulette").
        :param diversity_threshold: Minimum diversity before stopping early.
        :param crossover_method: Crossover type ("one_point_crossover", "multi_point_crossover", "uniform_crossover").
        """
        self.items = items
        self.capacity = capacity
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        self.selection_method = selection_method
        self.diversity_threshold = diversity_threshold
        self.crossover_method = crossover_method
        self.num_parents = 2
        self.population = self.generate_initial_population(len(items))

    def set_problem(self, items, capacity):
        """ Set a new knapsack problem with updated items and capacity. """
        self.items = items
        self.capacity = capacity
        self.population = self.generate_initial_population(len(self.items))

    def generate_initial_population(self, items_length):
        """ Generate an initial random population. """
        return [[random.choice([0, 1]) for _ in range(items_length)] for _ in range(self.population_size)]

    def calculate_fitness(self, individual):
        """ Calculate fitness (total value) of an individual while ensuring weight limit. """
        total_value, total_weight = 0, 0
        for i, gene in enumerate(individual):
            if gene:
                item = self.items[i]
                if total_weight + item["weight"] <= self.capacity:
                    total_value += item["value"]
                    total_weight += item["weight"]
                else:
                    return -1  # Invalid solution if overweight
        return total_value

    def select_parents(self):
        """ Parent selection method based on tournament or roulette strategy. """
        if self.selection_method == "tournament":
            return self.tournament_selection()
        elif self.selection_method == "roulette":
            return self.roulette_wheel_selection()
        else:
            raise ValueError("Invalid selection method")

    def tournament_selection(self):
        """ Tournament selection with randomness to maintain diversity. """
        parents = []
        for _ in range(self.num_parents):
            candidates = random.sample(self.population, min(5, len(self.population)))
            winner = random.choice(candidates[:3])  # Pick randomly from the top 3
            parents.append(winner)
        return parents

    def roulette_wheel_selection(self):
        """ Roulette wheel selection based on fitness proportion. """
        total_fitness = sum(max(0, self.calculate_fitness(ind)) for ind in self.population)
        if total_fitness == 0:
            return random.sample(self.population, self.num_parents)

        probabilities, cumulative_prob = [], 0
        for individual in self.population:
            fitness = max(0, self.calculate_fitness(individual))
            probability = fitness / total_fitness if total_fitness else 0
            cumulative_prob += probability
            probabilities.append((individual, cumulative_prob))

        parents = []
        for _ in range(self.num_parents):
            r = random.random()
            for individual, cum_prob in probabilities:
                if r <= cum_prob:
                    parents.append(individual)
                    break
        return parents

    def crossover(self, parents):
        """ Apply crossover method to generate offspring. """
        if self.crossover_method == "one_point_crossover":
            return self.one_point_crossover(parents)
        elif self.crossover_method == "uniform_crossover":
            return self.uniform_crossover(parents)
        else:
            raise ValueError("Invalid crossover method")

    def one_point_crossover(self, parents):
        parent1, parent2 = parents
        point = random.randint(1, len(self.items) - 1)

        if random.random() < self.crossover_rate:
            offspring1 = parent1[:point] + parent2[point:]
            offspring2 = parent2[:point] + parent1[point:]
        else:
            offspring1, offspring2 = parent1, parent2
        

        return [offspring1, offspring2]

    def uniform_crossover(self, parents):
        offspring = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i+1] if i+1 < len(parents) else parents[0]
            child1, child2 = [], []
            for j in range(len(parent1)):
                if random.random() < 0.5:
                    child1.append(parent1[j])
                    child2.append(parent2[j])
                else:
                    child1.append(parent2[j])
                    child2.append(parent1[j])
            offspring.extend([child1, child2])
        return offspring

    def mutation_update(self, population):
        diversity = self.check_diversity()
        mutation_rate = self.mutation_rate * 2 if diversity < 0.2 else self.mutation_rate

        for individual in population:
            if random.random() < mutation_rate:
                mutation_index = random.randint(0, len(individual) - 1)
                individual[mutation_index] = 1 - individual[mutation_index]


    def check_diversity(self):
        """ Calculate diversity as the percentage of unique individuals. """
        unique_individuals = {tuple(ind) for ind in self.population}
        diversity_score = len(unique_individuals) / self.population_size
        return diversity_score

    def terminate_early(self):
        """ Stop if diversity is too low for too long. """
        return self.check_diversity() < self.diversity_threshold

    def create_new_generation(self, offspring):
        """ Create a new generation with elitism and mutation. """
        elite_count = max(1, int(self.population_size * 0.1))
        new_population = self.population[:elite_count] + offspring[:self.population_size - elite_count]
        self.mutation_update(new_population)
        self.population = new_population

    def run(self):
        best_individual, best_fitness = None, -float('inf')

        for _ in range(self.generations):

            parents = self.select_parents()
            offspring = self.crossover(parents)
            self.create_new_generation(offspring)

            current_best = max(self.population, key=self.calculate_fitness)
            current_best_fitness = self.calculate_fitness(current_best)

            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                best_individual = current_best

            diversity = self.check_diversity()

            if diversity < 0.2:
                if self.mutation_rate < 0.5:  
                    self.mutation_rate = min(self.mutation_rate * 1.2, 0.5)
            elif diversity > 0.4:  
                self.mutation_rate = max(self.mutation_rate * 0.9, 0.05)


        print("\n✅ Best individual found:")
        print(best_individual)
        print(f"✅ Best fitness: {best_fitness}")
        return best_individual, best_fitness

