import random
import time
class KnapsackProblem1:

    # constructor of the class 
    #assigne the dataset to the Objects and the maximum number of individus in a population
    def __init__(self, Objects, ndiv, weight, crossoverRate, mutationRate, time_limit) -> None:
        self.Objects = Objects #values assigned for each object, look at the dataset
        self.ndiv = ndiv #number of individus
        self.population = [] #The first population (solutions)
        self.weight = weight #Maximum weight
        self.purposes = [] #An array to save the fitness values of each individu
        self.crossoverRate = crossoverRate #The rate of crossover
        self.mutationRate = mutationRate #The rate of mutation
        self.time_limit = time_limit #limiting the execution time
    #Lets define a function who can generate a population of ndiv individus
    #this function allow us to create our first set of solutions (population)   
    def generate_population(self):
        total_obj = len(self.Objects)
        i = 0
        while i < self.ndiv:
            total_weight = 0
            l = [0] * total_obj  # initialization with an empty solution
            # generating indexes
            indices = list(range(total_obj))
            random.shuffle(indices)  # mix the indexes to keep it random
            #we keep the good solutions
            for j in indices:
                if total_weight + self.Objects[j, 1] <= self.weight:
                    l[j] = 1
                    total_weight += self.Objects[j, 1]

            self.population.append(l.copy()) #add the solution to the initial population
            i += 1  

            
    #Now we must define our function of fitness
    def calculate_weight(self,solution):
        return sum(obj[1] for obj, sol in zip(self.Objects, solution) if sol == 1)
    def calculate_value(self,solution):
        return sum(obj[0] for obj, sol in zip(self.Objects, solution) if sol == 1)
    
    #If it's 0 then it's not considered as a solution (false) else we gonna calculate the value
    def fitness(self):
        self.purposes = [].copy() 
        for p in self.population:
            total_weight = self.calculate_weight(p)
            total_value = self.calculate_value(p)
            #Adding penality
            if (total_weight > self.weight):
                self.purposes.append(0)   #in case where the total weight is over the max weight
            else:
                self.purposes.append(total_value)   #in case where the total weight does not be over the max weight
    def select(self):
        if sum(self.purposes) == 0:  # verifiying if the fitnesses of the population is null
            return random.choice(self.population)  # select a random individu
        r = random.randint(0, sum(self.purposes)) #probability
        s = 0
        i = 0
        if r == 0:  # select the first individu 
            return self.population[0] 
        #wheel selection
        while s < r and i < len(self.purposes):
            s += self.purposes[i]
            i += 1
        return self.population[i - 1]
        
    #select two parents for the crossover part
    def selectParents(self):
        parent1 = self.select()
        parent2 = self.select()
        while(parent1 == parent2):
            parent2 = self.select()
        
        parents = {'firstParent' : parent1, 'secondParent' : parent2}
        return parents

    def crossover(self):
        r = random.uniform(0, 1)
        parents = self.selectParents()
        parent1 = parents['firstParent']
        parent2 = parents['secondParent']
        #In case where crossover didn't work
        childs = [parent1.copy(), parent2.copy()]  

        if r < self.crossoverRate:
            child1 = []
            child2 = []
            for i in range(len(parent1)):
                if random.uniform(0, 1) < 0.5:
                    child1.append(parent1[i])
                    child2.append(parent2[i])
                else:
                    child1.append(parent2[i])
                    child2.append(parent1[i])

            childs = [child1, child2]
        return childs

    #utation part
    def mutation(self, childs):
        r = random.uniform(0, 1)
        for child in childs:
            if random.uniform(0, 1) < self.mutationRate:  
                num_mutations = max(1, int(0.3 * len(self.Objects)))
                mutation_points = random.sample(range(len(self.Objects)), num_mutations)
                for point in mutation_points:
                    child[point] = 1 - child[point]
        return childs  
    
    
    
    def GA_Algorithm(self,max_generations,scale,elitism_rate):
        start_time = time.time()
        self.generate_population()
        self.fitness()
        best = max(self.purposes)
        solution = self.population[self.purposes.index(best)]
        elite_size = max(1, int(self.ndiv * elitism_rate))  # at Minimum 1 
        for x in range(1,max_generations):
            l=0
            next_pop = []
            sorted_indices = sorted(range(len(self.purposes)), key=lambda i: self.purposes[i], reverse=True)
            elites = [self.population[i] for i in sorted_indices[:elite_size]]
            next_pop.extend(elites)
            l = len(elites)
            while(l<self.ndiv):
                childs = self.crossover()
                childs_after_mutation = self.mutation(childs)
                next_pop.append(childs_after_mutation[0])
                l+=1
                if(l>=self.ndiv): break
                else:
                    next_pop.append(childs_after_mutation[1])
                    l+=1
                    if(l>=self.ndiv): break
            self.population = next_pop.copy()
            self.fitness()
            current_best = max(self.purposes)
            current_solution = self.population[self.purposes.index(current_best)]
            if(current_best>best):
                solution = current_solution.copy()
                best = current_best
        if(best!=0):
            print("value : ",best,"\nreal value : ",self.calculate_value(solution),"\nweight : ", self.calculate_weight(solution))
            if(scale == "La"):
                with open("results_large_scale_sol1.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(best) + "/ number individus = "+ str(self.ndiv) +"\n"
                    fichier.write(msg)
                    solution = "solution is : " + str(solution) +"\n"
                    fichier.write(solution)
                    print("Execution time :", time.time()-start_time)
                return
            if(scale == "Lo"):
                with open("results_low_scale_sol1.txt", "a") as fichier:
                    msg = "capacity : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(best) + "/ number individus = "+ str(self.ndiv) +"\n"
                    fichier.write(msg)
                    solution = "solution is : " + str(solution) +"\n"
                    fichier.write(solution)
                    print("Execution time :", time.time()-start_time)
                return
            if(scale == "Exe"):
                with open("Execution_time.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(best) + "/ number individus = "+ str(self.ndiv) + " execution time : " +str(time.time() - start_time)+ "\n"
                    fichier.write(msg)
        else:
            print("No solution found")
        print("Execution time :", time.time() - start_time)