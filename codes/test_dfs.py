from DFS import DFS
import pandas as pd
import numpy as np

#here u can the change the path to the path of the dataset
path = "C:\\Users\\sofia\\OneDrive\\Bureau\\Projet metah\\instances_01_KP\\large_scale\\knapPI_1_100_1000_1"

# Reading the file and storing the data in a list
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# transform the data into numbers instead of strings
data = [list(map(float, line.strip().split())) for line in lines]  # Convertir chaque valeur en float

df = np.array(data, dtype=float)
#for the data with a large scale we remove the last line because it's represent the optimal solution
df = df[1:, :]  # deleting the first line

sol = DFS(995,df,10)
sol.solve_with_dfs()
