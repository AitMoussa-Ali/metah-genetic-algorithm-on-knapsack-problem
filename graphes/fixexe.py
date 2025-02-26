import numpy as np
import matplotlib.pyplot as plt

# Données
temps_dexecution = [10, 30, 50, 70, 90, 110]
GA = [42216.0, 42243.0, 42620.0, 45405, 45602.0, 46347.0]
DFS = [11637.0, 12338.0, 12338.0, 12338.0, 12338.0, 12338.0]
objectif = 54503
# Largeur des barres
largeur = 8  

# Position des barres
x = np.array(temps_dexecution)
x_GA = x - largeur / 2  
x_DFS = x + largeur / 2  

# Création de l'histogramme
plt.figure(figsize=(10, 6))
bars_GA = plt.bar(x_GA, GA, width=largeur, color='blue', alpha=0.7, label="GA")
bars_DFS = plt.bar(x_DFS, DFS, width=largeur, color='red', alpha=0.7, label="DFS")
plt.axhline(y=objectif, color='red', linestyle='dashed', linewidth=2, label="Valeur optimale (54503)")

# Ajout des valeurs sur les barres
for bar in bars_GA:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), 
             ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

for bar in bars_DFS:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), 
             ha='center', va='bottom', fontsize=10, color='black', fontweight='bold')

# Labels et titre
plt.xlabel("Temps d'exécution (s)")
plt.ylabel("Valeur obtenue")
plt.title("Comparaison des performances entre GA et DFS pour un dataset de 1000 objets")
plt.xticks(temps_dexecution)  # Placer les ticks de l'axe X sur les temps
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Affichage
plt.show()
