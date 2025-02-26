import random
import time
class Sac_a_dos_dfs:
    def __init__(self, objets, weight, execution_time):
        self.objets = objets  # (valeur, poids)
        self.weight = weight  
        self.valeur = 0
        self.solution = []
        self.execution_time = execution_time
    def calc_poids_utilite(self, solution):
        poids = sum(self.objets[i][1] for i in range(len(solution)) if solution[i] == 1)
        valeur = sum(self.objets[i][0] for i in range(len(solution)) if solution[i] == 1)
        return poids, valeur

    def sad(self,start_time):
        solution = [0] * len(self.objets)  # initialisation aucun objet choisi
        pile = [(solution, 0)]  # niveau 0
        m_valeur = 0
        m_solution = []
        m_poids = 0
        while pile: 
            if(time.time()-start_time > self.execution_time) : break
            c_solution, niveau = pile.pop()  
            poids, valeur = self.calc_poids_utilite(c_solution)
            if poids <= self.weight:
                if valeur > m_valeur:  # si on trouve une meilleure valeur
                    m_valeur = valeur
                    m_solution = c_solution
                    m_poids = poids
                if niveau < len(self.objets):  # reste des objets 
                    pile.append((c_solution[:], niveau + 1))
                    obj_poids, obj_valeur = self.objets[niveau]
                    c_solution[niveau] = 1
                    pile.append((c_solution[:], niveau + 1))

        self.valeur = m_valeur  
        self.solution = m_solution[:]
        return m_solution, m_valeur, m_poids

    def evaluate(self, solution):
        poids, valeur = self.calc_poids_utilite(solution)
        if poids > self.weight:
            print("Erreur : Le poids total dépasse la capacité du sac.")
            return False
        else:
            print(f"Poids total : {poids}, Valeur totale : {valeur}")
            return True
        
    def affich(self):
        start_time = time.time()
        solution, valeur, poids  = self.sad(start_time)
        # print("temps exe :", time.time() - start_time)
        print("Solution trouvée avec DFS :")
        print(solution)
        print("Valeur totale :", valeur)
        print("Poids total :", poids)