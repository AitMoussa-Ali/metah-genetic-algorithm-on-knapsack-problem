import matplotlib.pyplot as plt
# import seaborn as sns

# # Activer le style seaborn pour une meilleure présentation
# sns.set_style("whitegrid")

# Données
instance = [10, 15, 20, 23, 100, 200] 
temps_GA = [0.004, 0.0148, 0.025, 0.6, 5.199, 3.577] 
temps_DFS = [0.005, 0.23, 14.34, 90.175, 900, 18000]

# Création du graphique
plt.figure(figsize=(9, 5))

# Courbes avec un design plus esthétique
plt.plot(instance, temps_GA, marker='o', linestyle='-', color='#007acc', markersize=5, linewidth=2, label='GA (Algorithme Génétique)')
plt.plot(instance, temps_DFS, marker='o', linestyle='-', color='#ff5733', markersize=5, linewidth=2, label='DFS')

# Améliorations visuelles
plt.xlabel("Taille de l'instance", fontsize=12, fontweight='bold')
plt.ylabel("Temps d'exécution (secondes)", fontsize=12, fontweight='bold')
plt.yscale("log")  # Échelle logarithmique pour mieux voir la différence
# plt.xscale("log")  # Échelle logarithmique pour mieux voir la différence
plt.title("Comparaison des temps d'exécution : GA vs DFS", fontsize=10, fontweight='bold')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(fontsize=10, loc="upper left", frameon=True, fancybox=True, shadow=True, borderpad=1)

# Ajouter un fond avec un léger quadrillage
plt.grid(True, which="both", linestyle="-", linewidth=0.6, alpha=0.15, color = "black")

# Affichage du graphique
plt.show()
#crossover = 0.8
#mutation = 0.01
#ndiv = 100
#elitism = 0.1
#generation=30