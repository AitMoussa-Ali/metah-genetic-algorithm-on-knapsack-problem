import random

class KnapsackProblem1:

    # constructor of the class 
    #assigne the dataset to the Objets and the maximum number of individus in a population
    def __init__(self, Objets, ndiv, weight, crossoverRate, mutationRate) -> None:
        self.Objets = Objets #values assigned for each object, look at the dataset
        self.ndiv = ndiv #number of individus
        self.population = [] #The first population (solutions)
        self.weight = weight #Maximum weight
        self.purposes = [] #An array to save the fitness values of each individu
        self.crossoverRate = crossoverRate #The rate of crossover
        self.mutationRate = mutationRate #The rate of mutation
        
    #Lets define a function who can generate a population of ndiv individus
    #this function allow us to create our first set of solutions (population)   
    def generate_population(self):
        total_obj = len(self.Objets)
        i = 0
        while i < self.ndiv:
            total_weight = 0
            l = [0] * total_obj  # initialization with an empty solution
            # generating indexes
            indices = list(range(total_obj))
            random.shuffle(indices)  # mix the indexes to keep it random
            #we keep the good solutions
            for j in indices:
                if total_weight + self.Objets[j, 1] <= self.weight:
                    l[j] = 1
                    total_weight += self.Objets[j, 1]

            self.population.append(l) #add the solution to the initial population
            i += 1  
            
            
    #Now we must define our function of fitness
    #If it's 0 then it's not considered as a solution (false) else we gonna calculate the value
    def fitness(self):
        for p in self.population : 
            total_weight = 0
            total_value = 0
            for i in range(0,len(p)):
                if(p[i] != 0):
                    total_weight = total_weight+self.Objets[i,1] #second column represente the weight
                    total_value = total_value+self.Objets[i,0] #first column represente the value
            if(total_weight <= self.weight):
                self.purposes.append(total_value) #in case where the total weight does not be over the max weight
            else:
                self.purposes.append(0) #in case where the total weight is over the max weight
    
    
    #Cette fonction permet de selectionner un individu avec une proba generer par random
    #On utilise la methode de selction par roulette
    def select(self):
        if sum(self.purposes) == 0:  # vérifier si la somme des fitness est nulle
            return random.choice(self.population)  # Sélectionne un individu aléatoire
        r = random.randint(0, int(sum(self.purposes)))
        s = 0
        i = 0
        if r == 0:  # Gérer explicitement le cas où r == 0
            return self.population[0]  # Choisir le premier individu
    
        while s < r and i < len(self.purposes):
            s += self.purposes[i]
            i += 1
        return self.population[i - 1]
        
    #cette fonction permet de selectionner deux parents qui soit toujours different pour garantir une bonne convergence
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
        childs = [parent1, parent2]

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

            childs = [child1,child2]

        return childs
        
    def mutation(self, childs):
        r = random.uniform(0, 1)
        if r < self.mutationRate:
            for child in childs:
                num_mutations = max(1, int(0.3 * len(child)))  # Muter 30% des gènes
                mutation_points = random.sample(range(len(child)), num_mutations)
                for point in mutation_points:
                    child[point] = 1 - child[point]  # Flip le bit
        return childs 
    
    def GA_Algorithm(self,max_generations,scale):
        generation = 0
        best_fitness = 0
        fitnesses = []
        self.generate_population()
        all_population = []
        best = 0
        while(generation < max_generations):
            self.fitness()
            current_best = max(self.purposes)
            if(current_best > best_fitness):
                best_fitness = current_best
                best = generation                
            next_population = []
            l = 0
            while(l < self.ndiv):
                childs = self.crossover()
                childs = self.mutation(childs)
                for c in childs:
                    next_population.append(c)
                    l+=1
                    
            all_population.append(self.population)
            
            self.population = next_population
            fitnesses.append(self.purposes)
            self.purposes = []
            generation+=1
            
        best_population = all_population[best]
        fit = fitnesses[best]
        if(scale == "La"):
            if(max(fitnesses[best])!=0):
                index = fit.index(max(fit))
                print("✅ the best solution is ", "at generation ", best, " with value 🎯 = ",max(fitnesses[best]))
                with open("results_large_scale_sol1.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(max(fitnesses[best])) + "/ number individus = "+ str(self.ndiv) +"\n"
                    fichier.write(msg)
                    solution = "solution is : " + str(best_population[index]) +"\n"
                    fichier.write(solution)
            else:
                print("No solution found")
        else:
            if(max(fitnesses[best])!=0):
                index = fit.index(max(fit))
                print("✅ the best solution is ", "at generation ", best, " with value 🎯 = ",max(fitnesses[best]))
                with open("results_low_scale_sol1.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(max(fitnesses[best])) + "/ number individus = "+ str(self.ndiv) +"\n"
                    fichier.write(msg)
                    solution = "solution is : " + str(best_population[index]) +"\n"
                    fichier.write(solution) 
            else:
                print("No solution found")
    
