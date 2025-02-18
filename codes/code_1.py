import random
class Sac_a_dos:

    # constructor of the class 
    #assigne the dataset to the Objets and the maximum number of individus in a population
    def __init__(self, Objets, ndiv, width) -> None:
        self.Objets = Objets #values assigned for each object, look at the dataset
        self.ndiv = ndiv #number of individus
        self.population = [] #The first population (solutions)
        self.width = width #Maximum width
        self.purposes = [] #An array to save the fitness values of each individu
        
        
    #Lets define a function who can generate a population of ndiv individus
    #this function allow us to create our first set of solutions (population)
    def generate_population(self):
        total_obj = len(self.Objets)
        i=0
        while(i < self.ndiv):
            total_width = 0
            l = []
            for j in range(0,total_obj):
                rand = random.randint(0,1)
                l.append(rand)
                if(rand == 1):
                    total_width = total_width+self.Objets[j,0]
                
            if(total_width<=self.width):
                self.population.append(l)
                i+=1    

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
                    
            self.purposes.append(total_value) #dans le cas ou elle respecte la contrainte on rajouter le poids totale a l'index
    
    
    #Cette fonction permet de selectionner un individu avec une proba generer par random
    #On utilise la methode de selction par roulette
    def select(self):
        #first we must generate a number between 0 and sum of fitness (totale de fitness)
        r = random.randint(0,sum(self.purposes))
        s=0
        i=0
        while(s < r and i < len(self.purposes)):
            s=s+self.purposes[i]
            i+=1
        return self.population[i-1]
        
        
    #cette fonction permet de selectionner deux parents qui soit toujours different pour garantir une bonne convergence
    def selectParents(self):
        parent1 = self.select()
        parent2 = self.select()
        while(parent1 == parent2):
            parent2 = self.select()
        
        parents = {'firstParent' : parent1, 'secondParent' : parent2}
        return parents
    
    
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