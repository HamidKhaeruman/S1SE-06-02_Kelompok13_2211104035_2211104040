import random
from chromosome import Chromosome

class Population:
    def __init__(self, size):
        self.individuals = [Chromosome() for _ in range(size)]

    def evaluate(self):
        return [ind.fitness for ind in self.individuals]

    def select(self, k=3):
        selected = []
        for _ in range(len(self.individuals)):
            aspirants = random.sample(self.individuals, k)
            winner = min(aspirants, key=lambda ind: ind.fitness)
            selected.append(winner)
        return selected

    def create_next_generation(self, selected, crossover_rate, mutation_rate):
        next_gen = []
        for i in range(0, len(selected), 2):
            parent1 = selected[i]
            parent2 = selected[(i+1) % len(selected)]
            child1 = parent1.crossover(parent2, crossover_rate)
            child2 = parent2.crossover(parent1, crossover_rate)
            child1.mutate(mutation_rate)
            child2.mutate(mutation_rate)
            next_gen.append(child1)
            next_gen.append(child2)
        self.individuals = next_gen[:len(self.individuals)]  # pastikan jumlah sama
