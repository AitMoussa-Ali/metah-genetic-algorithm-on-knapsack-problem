import csv
from DFS import DFS
from GA import GeneticAlgorithm
from Evaluation import GAEvaluation

def load_items_from_csv(file_path):
    items = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {
                "weight": int(row["Poids (kg)"]),
                "value": int(row["Valeur (€)"])
            }
            items.append(item)
    return items

def main():
    file_path = "train.csv"  
    items = load_items_from_csv(file_path)

    capacity = 17  

    print("Loaded items:", items)

    # Create solver instances
    dfs_solver = DFS()  
    ga_solver = GeneticAlgorithm(
        items, capacity,
        population_size=30,
        generations=100,
        mutation_rate=0.05,
        crossover_rate=0.8,
        elitism=True,
        selection_method="tournament",
        diversity_threshold=1,
        crossover_method="one_point_crossover"
    )
    dfs_solver.set_problem(items, capacity)
    ga_solver.set_problem(items, capacity)
    evo=GAEvaluation(ga_solver=ga_solver,problem_instances=[(items,capacity)],dfs_solver=dfs_solver)
    evo.compare_solvers()
    evo.plot_results()

if __name__ == "__main__":
    main()
