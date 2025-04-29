import random
import math

class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            self.genes = [random.uniform(-10, 10), random.uniform(-10, 10)]
        else:
            self.genes = [max(-10, min(10, genes[0])), max(-10, min(10, genes[1]))]
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        x1, x2 = self.genes
        try:
            result = -(math.sin(x1) * math.cos(x2) * math.tan(x1 + x2)) + (3/4) * math.exp(1 - math.sqrt(x1**2))
            return result
        except:
            return float('inf')  # Jika math error (seperti tan(x) tak terdefinisi)

    def crossover(self, partner, crossover_rate=0.8):
        if random.random() < crossover_rate:
            child_genes = [
                self.genes[i] if random.randint(0, 1) == 0 else partner.genes[i]
                for i in range(2)
            ]
        else:
            child_genes = self.genes.copy()
        return Chromosome(child_genes)

    def mutate(self, mutation_rate=0.1):
        if random.random() < mutation_rate:
            idx = random.randint(0, 1)
            self.genes[idx] += random.uniform(-1, 1)
            self.genes[idx] = max(-10, min(10, self.genes[idx]))
        self.fitness = self.calculate_fitness()
