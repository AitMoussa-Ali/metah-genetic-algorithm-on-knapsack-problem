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

            self.population.append(l) #add the solution to the initial population
            i += 1  
            
            
    #Now we must define our function of fitness
    #If it's 0 then it's not considered as a solution (false) else we gonna calculate the value
    def fitness(self):
        self.purposes = []
        for p in self.population : 
            total_weight = 0
            total_value = 0
            for i in range(0,len(p)):
                total_weight = total_weight+self.Objects[i,1]*p[i] #second column represente the weight
                total_value = total_value+self.Objects[i,0]*p[i] #first column represente the value
            if(total_weight <= self.weight):
                self.purposes.append(total_value) #in case where the total weight does not be over the max weight
            else:
                self.purposes.append(float(0)) #in case where the total weight is over the max weight
    
    
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
                num_mutations = max(1, int(0.1 * len(child)))  # Muter 10% des gènes
                mutation_points = random.sample(range(len(child)), num_mutations)
                for point in mutation_points:
                    child[point] = 1 - child[point]  # Flip le bit
        return childs 
    
    def calculate_weight(self,solution):
        return sum(obj[1] for obj, sol in zip(self.Objects, solution) if sol == 1)
    
    
    def GA_Algorithm(self,max_generations,scale,elitism_rate):
        generation = 0
        best_fitness = 0
        fitnesses = []
        self.generate_population()
        all_population = []
        best = 0
        start_time = time.time()
        while(generation < max_generations):
            # if(time.time() - start_time > self.time_limit):
            #     break
            self.fitness()
            fitnesses.append(self.purposes.copy())
            all_population.append(self.population.copy())
            current_best = max(self.purposes)
            index = self.purposes.index(current_best)
            sol = self.population[index]
            if(current_best > best_fitness and self.calculate_weight(sol) <= self.weight ):
                best_fitness = current_best
                best = generation                
            next_population = []
            sorted_population = [x for _, x in sorted(zip(self.purposes, self.population), reverse=True)]
            #elitism
            num_elite = int(elitism_rate * self.ndiv)  
            next_population = sorted_population[:num_elite]  
            l = 0
            while(l < self.ndiv):
                childs = self.crossover()
                childs = self.mutation(childs)
                for c in childs:
                    if self.calculate_weight(c) <= self.weight:
                        next_population.append(c)
                        l+=1
            self.population = next_population.copy()
            self.purposes = []
            generation+=1
            
        best_population = all_population[best]
        fit = fitnesses[best]
        index = fit.index(max(fit))
        # print(fit)
        # print(best_population)
        # print(best_population[index])
        if(max(fitnesses[best])!=0):
            print("the best solution is", " at generation ", best, " with value = ",max(fitnesses[best]), "and weight : ",self.calculate_weight(best_population[index]))
            if(scale == "La"):
                with open("results_large_scale_sol1.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(max(fitnesses[best])) + "/ number individus = "+ str(self.ndiv) +"\n"
                    fichier.write(msg)
                    solution = "solution is : " + str(best_population[index]) +"\n"
                    fichier.write(solution)
                    print("Execution time :", time.time()-start_time)
                return
            if(scale == "Lo"):
                with open("results_low_scale_sol1.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(max(fitnesses[best])) + "/ number individus = "+ str(self.ndiv) +"\n"
                    fichier.write(msg)
                    solution = "solution is : " + str(best_population[index]) +"\n"
                    fichier.write(solution)
                    print("Execution time :", time.time()-start_time)
                return
            if(scale == "Exe"):
                with open("Execution_time.txt", "a") as fichier:
                    msg = "weight : " + str(self.weight) + " / crossover = " + str(self.crossoverRate) + " / mutation = " + str(self.mutationRate) + " / generations = " + str(max_generations) + " / value = "+str(max(fitnesses[best])) + "/ number individus = "+ str(self.ndiv) + " execution time : " +str(time.time() - start_time)+ "\n"
                    fichier.write(msg)
        else:
            print("No solution found")
        print("Execution time :", time.time() - start_time)
