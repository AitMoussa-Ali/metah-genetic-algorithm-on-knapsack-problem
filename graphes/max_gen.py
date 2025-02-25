import matplotlib.pyplot as plt

# Données
nbr_generation = [10, 20, 30, 40, 50]
values = [7546, 8497, 9019, 8423, 8401]
objectif = 9147  # Valeur cible

# Création du graphique avec des barres plus larges
plt.figure(figsize=(8, 5))
bars = plt.bar(nbr_generation, values, color='blue', alpha=0.7, width=5, label="Valeurs trouvées")  # Augmenter width

# Ligne pour la valeur optimale
plt.axhline(y=objectif, color='red', linestyle='dashed', linewidth=2, label="Valeur optimale (9147)")

# Ajout des valeurs à l'intérieur des barres
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, value - 200, str(value), 
             ha='center', va='center', fontsize=10, color='white', fontweight='bold')

# Titres et légendes
plt.xlabel("Nombre de Générations")
plt.ylabel("Valeur trouvée")
plt.title("Évolution des Résultats en Fonction du Nombre de Générations")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Affichage du graphique
plt.show()
#crossover = 0.8
#mutation = 0.01
#ndiv = 100
#elitism = 0.1