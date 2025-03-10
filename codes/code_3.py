import random

class Sac_a_dos_dfs:
    def __init__(self, objets, width):
        self.objets = objets  # (valeur, poids)
        self.width = width  
        self.valeur = 0
        self.solution = []

    def calc_poids_utilite(self, solution):
        poids = sum(self.objets[i][1] for i in range(len(solution)) if solution[i] == 1)
        valeur = sum(self.objets[i][0] for i in range(len(solution)) if solution[i] == 1)
        return poids, valeur

    def sad(self):
        solution = [0] * len(self.objets)  # initialisation aucun objet choisi
        pile = [(solution, 0)]  # niveau 0
        m_valeur = 0
        m_solution = []

        while pile: 
            c_solution, niveau = pile.pop()  
            poids, valeur = self.calc_poids_utilite(c_solution)
            if poids <= self.width:
                if valeur > m_valeur:  # si on trouve une meilleure valeur
                    m_valeur = valeur
                    m_solution = c_solution

                if niveau < len(self.objets):  # reste des objets 
                    pile.append((c_solution[:], niveau + 1))
                    c_solution[niveau] = 1
                    pile.append((c_solution[:], niveau + 1))

        self.valeur = m_valeur  
        self.solution = m_solution[:]
        return m_solution, m_valeur

    def evaluate(self, solution):
        poids, valeur = self.calc_poids_utilite(solution)
        if poids > self.width:
            print("Erreur : Le poids total dépasse la capacité du sac.")
            return False
        else:
            print(f"Poids total : {poids}, Valeur totale : {valeur}")
            return True
        
    def affich(self):
        solution, valeur = self.sad()
        print("Solution trouvée avec DFS :")
        print(solution)
        print("Valeur totale :", valeur)
        poids_total = sum(self.objets[i][1] for i in range(len(solution)) if solution[i] == 1)
        print("Poids total :", poids_total)

        if self.evaluate(solution):
            print("Solution valide.")
        else:
            print("Solution invalide.")
