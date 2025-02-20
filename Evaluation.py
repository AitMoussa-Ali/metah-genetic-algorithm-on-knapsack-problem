import matplotlib.pyplot as plt

class GAEvaluation: 
    def __init__(self, ga_solver, problem_instances, dfs_solver):
        """ 
        Parameters: 
            - ga_solver: An instance of the GeneticAlgorithm class.
            - dfs_solver: An instance of the DFS class.
            - problem_instances: A list of problem instances,
              each a dictionary with keys "items" and "capacity". 
        """
        self.ga_solver = ga_solver
        self.dfs_solver = dfs_solver
        self.problem_instances = problem_instances
        self.results = {}
    
    def tune_parameters(self, param_grid):
        """ Tune GA parameters and evaluate performance for each parameter set. """
        results = {}
        for params in param_grid:
            self.ga_solver.set_parameters(**params)
            best_individual, best_fitness = self.ga_solver.run()
            results[str(params)] = {'best_fitness': best_fitness, 'best_individual': best_individual}
        return results

    def compare_solvers(self):
        """ Compare DFS and GA on the given problem instances. """
        for idx, instance in enumerate(self.problem_instances):
            items, capacity = instance
            self.dfs_solver.set_problem(items, capacity)
            dfs_sol, dfs_val = self.dfs_solver.run()
            self.ga_solver.set_problem(items, capacity)
            ga_sol, ga_val = self.ga_solver.run()
            self.results[f"Instance_{idx+1}"] = {
                "DFS": {"solution": dfs_sol, "value": dfs_val},
                "GA": {"solution": ga_sol, "value": ga_val}
            }
        return self.results

    def show_Results(self):
        """ Print the best solution and fitness for each solver. """
        if not self.results:
            print("No results to show. Run `compare_solvers()` first.")
            return

        for instance, results in self.results.items():
            print(f"\n--- Problem Instance: {instance} ---")
            print(f"DFS Solution: {results['DFS']['solution']}")
            print(f"DFS Value: {results['DFS']['value']}")
            print(f"GA Solution: {results['GA']['solution']}")
            print(f"GA Value: {results['GA']['value']}\n")
    def plot_results(self):
        """ Plot a bar chart comparing DFS and GA results. """
        if not self.results:
            print("No results to plot. Run `compare_solvers()` first.")
            return
        
        instances = list(self.results.keys())
        dfs_values = [self.results[inst]["DFS"]["value"] for inst in instances]
        ga_values = [self.results[inst]["GA"]["value"] for inst in instances]

        x = range(len(instances))

        plt.figure(figsize=(10, 5))
        plt.bar(x, dfs_values, width=0.4, label="DFS", color="blue", align="center")
        plt.bar([i + 0.4 for i in x], ga_values, width=0.4, label="GA", color="orange", align="center")

        plt.xlabel("Problem Instance")
        plt.ylabel("Total Value Achieved")
        plt.title("DFS vs Genetic Algorithm Performance")
        plt.xticks([i + 0.2 for i in x], instances)
        plt.legend()
        plt.show()
