import random
class DFS : 
    #constructor
    def __init__(self,max_width,Objects):
        self.width = max_width
        self.Objets = Objects
        self.solutions = []
    
    #Function to calculate the value of all the solutions (for each solution)    
    def calculate_values(self):
        values = []
        for x in self.solutions:
            value = 0
            for i in range(len(x)):
                value += x[i]*self.Objets[i][0]
            values.append(value)
        return values
     
    #Function to calculate the width of a solution
    def calculate_width(self,solution):
        width = 0
        for i in range(len(solution)):
            width += solution[i]*self.Objets[i][1]
        return width
    
    #Function DFS who explore all the possibilities of the problem
    def DFS(self,index,solution):
        if(index == len(self.Objets)):
            if(self.calculate_width(solution)<=self.width):
                self.solutions.append(solution[:])
            return 
        solution[index] = 0
        self.DFS(index+1,solution)
        solution[index] = 1
        self.DFS(index+1,solution)
    
    #Function to find the solution using DFS
    def find_solution(self):
        self.DFS(0,[0]*len(self.Objets))
        values = self.calculate_values()
        index = values.index(max(values))
        print("✅ solution find with sucess :", self.solutions[index]," with value 🎯 = ",max(values))
       
        
        
     