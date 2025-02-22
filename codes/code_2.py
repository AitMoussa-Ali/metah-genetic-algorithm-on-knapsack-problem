import random
class Sac_a_dos_2:

    # constructor of the class 
    #assigne the dataset to the Objets and the maximum number of individus in a population
    def __init__(self, Objets, ndiv, width) -> None:
        self.Objets = Objets #values assigned for each object, look at the dataset
        self.ndiv = ndiv #number of individus
        self.population = [] #The first population (solutions)
        self.width = width #Maximum width
        self.purposes = [] #An array to save the fitness values of each individu
        self.crossoverRate = 0.8 #The rate of crossover
        self.mutationRate = 0.1 #The rate of mutation
        
    #Lets define a function who can generate a population of ndiv individus
    #this function allow us to create our first set of solutions (population)
    #Now we gonna use the gluton algorithm to generate the first population
    
    def generate_population(self):
        sorted_indices = sorted(range(len(self.Objets)), key=lambda i: self.Objets[i][0] / self.Objets[i][1], reverse=True)
        for _ in range(self.ndiv):
            random.shuffle(sorted_indices)
            
            solution = [0] * len(self.Objets)
            total_width = 0
            
            for i in sorted_indices:
                value, weight = self.Objets[i]
                if(total_width + weight <= self.width):
                    solution[i] = 1
                    total_width += weight
            self.population.append(solution)

    #Now we must define our function of fitness
    #If it's 0 then it's not considered as a solution (false)
    #pour comprendre cette fonction, notre probleme consiste a maximiser la valeur et minimiser le poids
    #et donc les solutions qu'on vas prendre, on vas prendre que les solutions qui respecte la contrainte du poids
    #alors le fitness est definie seulement sur la valeur car on chercher a la maximiser
    def fitness(self):
        for p in self.population : 
            total_width = 0
            total_value = 0
            for i in range(0,len(p)):
                if(p[i] != 0):
                    total_width = total_width+self.Objets[i,0] #first column represente the width
                    total_value = total_value+self.Objets[i,1] #second column represente the value
            if(total_width <= self.width):
                self.purposes.append(total_value) #dans le cas ou elle respecte la contrainte on rajouter le poids totale a l'index
            else:
                self.purposes.append(0) #dans le cas ou elle ne respecte pas la contrainte on rajoute 0 a l'index
    
    
    #Cette fonction permet de selectionner un individu avec une proba generer par random
    #On utilise la methode de selction par roulette
    def select(self):
        if sum(self.purposes) == 0:  # vérifier si la somme des fitness est nulle
            return random.choice(self.population)  # Sélectionne un individu aléatoire
        r = random.randint(0, sum(self.purposes))
        s = 0
        i = 0
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
        childs = [parent1,parent2]
        if r < self.crossoverRate:
            # Assure un point de croisement raisonnable, éviter la fin ou le début
            crossover_point1 = random.randint(1, len(parent1) - 2)
            crossover_point2 = random.randint(crossover_point1 + 1, len(parent1) - 1)
                
            # Créer les enfants via crossover
            child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
            child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
            childs = [child1,child2]
        
        return childs
        
    def mutation(self,childs):
        r = random.uniform(0,1)
        if(r < self.mutationRate):
            child1 = childs[0]
            child2 = childs[1]
            mutation_point = random.randint(0, len(child1) - 1)
            child1[mutation_point] = 1 - child1[mutation_point]
            child2[mutation_point] = 1 - child2[mutation_point]
        
        return childs   
    
    def GA_Algorithm(self,max_generations,stagnation_threshold):
        generation = 0
        stagnation_counter = 0  
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
                stagnation_counter = 0
            else:
                stagnation_counter += 1
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
        if(max(fitnesses[best])!=0):
            print("fitness : ", max(fitnesses[best]), " at generation ", best)
            index = fit.index(max(fit))
            #print("the best solution is", best_population[index])
            with open("results.txt", "a") as fichier:
                fichier.write(str(max(fitnesses[best]))+"\n")
        else:
            print("No solution found")
        
        
    #Cette fonction pour l'instant permet d'afficher les differents resultats des fonctions precedente
    #Vous pouvez refaire l'execution plusieurs fois
    def printing(self):
        print("the data set")
        print(self.Objets)
        print("The number of individus")
        print(self.ndiv)    
        print("the maximum width is :",self.width)
        print("The first population is :")
        for p in self.population:
            print(p)
        print("the fitness is :")
        for p in self.purposes:
            print(p)
        k = self.selectParents()
        print("the parents are ", k)