import matplotlib.pyplot as plt
import numpy as np

# Données
mutation = [0.01, 0.03, 0.05, 0.07, 0.09, 0.11]
values = [8887, 8217, 8258, 8857, 8603, 8806]
objectif = 9147  # Valeur cible

# Configuration du graphique
plt.figure(figsize=(10, 6))
bars = plt.bar(mutation, values, width=0.01, color='blue', edgecolor='black', alpha=0.7, label="Valeurs trouvées")
# Ligne pour la valeur optimale
plt.axhline(y=objectif, color='red', linestyle='dashed', linewidth=2, label="Valeur optimale (9147)")
# Ajouter les valeurs à l'intérieur des barres
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 200, 
             str(value), ha='center', va='top', fontsize=12, color='white', fontweight='bold')

# Labels et titre
plt.xlabel("Taux de Mutation", fontsize=14)
plt.ylabel("Valeur de l'optimisation", fontsize=14)
plt.title("Impact du taux de mutation sur la valeur obtenue", fontsize=16)
plt.legend()
# plt.xticks(mutation)  # Assure que les ticks sont alignés avec les valeurs de mutation

plt.grid(axis='y', linestyle='--', alpha=0.6)


# Affichage du graphique
plt.show()
#crossover = 0.8
#ndiv = 100
#elitism = 0.1
#generation = 30