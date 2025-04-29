from population import Population

class GeneticAlgorithm:
    def __init__(self, pop_size=50, generations=100, crossover_rate=0.8, mutation_rate=0.1):
        self.pop_size = pop_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = Population(self.pop_size)
        self.best_individual = None

    def run(self):
        for gen in range(self.generations):
            fitnesses = self.population.evaluate()
            best_idx = fitnesses.index(min(fitnesses))
            best_candidate = self.population.individuals[best_idx]

            if self.best_individual is None or best_candidate.fitness < self.best_individual.fitness:
                self.best_individual = best_candidate

            selected = self.population.select()
            self.population.create_next_generation(selected, self.crossover_rate, self.mutation_rate)

        return self.best_individual
