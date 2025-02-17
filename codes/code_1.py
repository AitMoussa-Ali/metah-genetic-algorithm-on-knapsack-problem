import random
class Sac_a_dos:

    # constructor of the class 
    #assigne the dataset to the Objets and the maximum number of individus in a population
    def __init__(self, Objets, ndiv, width) -> None:
        self.Objets = Objets
        self.ndiv = ndiv
        self.population = []
        self.width = width
        self.purposes = [] #An array to save the fitness values of each individu
        
        
    #Lets define a function who can generate a population of ndiv individus
    def generate_population(self):
        total_obj = len(self.Objets)
        for i in range(0,self.ndiv):
            l = []
            for j in range(0,total_obj):
                rand = random.randint(0,1)
                l.append(rand)
            self.population.append(l)        


    #Now we must define our function of fitness
    #If it's 0 then it's not considered as a solution
    def fitness(self):
        k=0
        for p in self.population :
            total_width = 0
            total_value = 0
            for i in range(0,len(p)):
                if(p[i] != 0):
                    total_width = total_width+self.Objets[i,0]
                    total_value = total_value+self.Objets[i,1]
            k+=1  
            if(total_width>self.width):
                self.purposes.append(0)
            else:
                self.purposes.append(total_value)
    
    
    #Now let's define a new function that'a select a couple of individu with a (la methode de roulette) 
    def select(self):
        #first we must generate a number between 0 and sum of fitness 
        r = random.randint(0,sum(self.purposes))
        s=0
        i=0
        while(s < r and i < len(self.purposes)):
            s=s+self.purposes[i]
            i+=1
        return self.population[i-1]
        
        
    def selectParents(self):
        parent1 = self.select()
        parent2 = self.select()
        while(parent1 == parent2):
            parent2 = self.select()
        
        parents = {'firstParent' : parent1, 'secondParent' : parent2}
        return parents
    
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