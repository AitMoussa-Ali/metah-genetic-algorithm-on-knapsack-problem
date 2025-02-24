import random
import time
class DFS : 
    #constructor
    def __init__(self,max_weight,Objects,time_limite):
        self.weight = max_weight
        self.Objets = Objects
        self.best_value = 0
        self.best_solution = []
        self.time_limite = time_limite
        self.start_time = 0
    #Function to calculate the value of all the solutions (for each solution)    
    def calculate_values(self):
        values = []
        for x in self.solutions:
            value = 0
            for i in range(len(x)):
                value += x[i]*self.Objets[i][0]
            values.append(value)
        return values
     
    #Function to calculate the weight of a solution
    def calculate_weight(self,solution):
        weight = 0
        for i in range(len(solution)):
            weight += solution[i]*self.Objets[i][1]
        return weight
    
    def calculate_value(self,solution):
       value = 0
       for i in range(len(solution)):
           value += solution[i]*self.Objets[i][0]
       return value
    
    #Function DFS who explore all the possibilities of the problem
    def DFS(self, index, solution):
        if(time.time() - self.start_time > self.time_limite) : 
            return
        if index == len(self.Objets):
            total_weight = self.calculate_weight(solution)
            total_value = self.calculate_value(solution)
            if total_weight <= self.weight and total_value > self.best_value:
                self.best_value = total_value
                self.best_solution = solution.copy()
            return  
        solution[index] = 0
        self.DFS(index + 1, solution)
        solution[index] = 1
        self.DFS(index + 1, solution)
    
    #Function to find the solution using DFS
    def solve_with_dfs(self):
        self.start_time = time.time()
        self.DFS(0,[0]*len(self.Objets))
        print("✅ solution find with sucess :", self.best_solution," with value 🎯 = ",self.best_value)
       
        
        
     