class DFS:
    def __init__(self, items=None, capacity=None): 
        self.items = items
        self.capacity = capacity
        self.best_value = 0
        self.best_solution = []
        
    def set_problem(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def calculate_weight_value(self, solution):
        total_weight = 0
        total_value = 0
        for i in range(len(solution)):
            if solution[i] == 1:
                total_weight += self.items[i]["weight"]
                total_value += self.items[i]["value"]
        return total_weight, total_value

    def run(self):
        if not self.items or not self.capacity:
            raise ValueError("Items or capacity not set")

        solution = [0] * len(self.items)
        stack = [(solution.copy(), 0)]
        
        while stack:
            current_sol, level = stack.pop()
            weight, value = self.calculate_weight_value(current_sol)

            if weight <= self.capacity:
                if value > self.best_value:
                    self.best_value = value
                    self.best_solution = current_sol.copy()

                if level < len(self.items):
                    stack.append((current_sol.copy(), level + 1))
                    new_sol = current_sol.copy()
                    new_sol[level] = 1
                    stack.append((new_sol, level + 1))

        return self.best_solution, self.best_value