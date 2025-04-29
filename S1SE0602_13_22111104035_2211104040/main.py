from genetic_algorithm import GeneticAlgorithm

def main():
    ga = GeneticAlgorithm(pop_size=50, generations=100, crossover_rate=0.8, mutation_rate=0.1)
    best = ga.run()

    print("=== HASIL AKHIR ===")
    print(f"Kromosom terbaik: {best.genes}")
    print(f"x1 = {best.genes[0]}, x2 = {best.genes[1]}")
    print(f"Nilai minimum fungsi: {best.fitness}")

if __name__ == "__main__":
    main()
