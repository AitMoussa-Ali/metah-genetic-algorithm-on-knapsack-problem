from code_1 import KnapsackProblem1
import pandas as pd
import numpy as np

#here u can the change the path to the path of the dataset
path = "C:\\Users\\sofia\\OneDrive\\Bureau\\Nouveau dossier\\instances_01_KP\\low-dimensional\\f3_l-d_kp_4_20"

# Reading the file and storing the data in a list
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# transform the data into numbers instead of strings
data = [list(map(int, line.strip().split())) for line in lines]  # Convertir chaque valeur en float

df = np.array(data, dtype=int)
#for the data with a large scale we remove the last line because it's represent the optimal solution
df = df[1:, :]  # deleting the first line

#last parameter is the percentage of mutation (not mutation rate)
sac = KnapsackProblem1(df, 5, 20, 0.8, 0.01, 110)
#parameteres are : 1/generations 2/.... 3/elitism rate 
sac.GA_Algorithm(30,"sd",0.15) #La for large scale and Lo for low scale Exe
