from code_1 import KnapsackProblem1
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

sac = KnapsackProblem1(df, 200, 995, 0.8, 0.01, 110)
# sac.generate_genome()
sac.GA_Algorithm(40,"Lo",0.1) #La for large scale and Lo for low scale Exe