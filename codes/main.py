# from code_1 import Sac_a_dos
# import pandas as pd

# dataset = pd.read_csv('C:\\Users\\sofia\\OneDrive\\Bureau\\ProjetMetaH\\codes\\sac_a_dos_dataset.csv')
# # print(dataset)
# X = dataset.iloc[:,1:].values

# sac = Sac_a_dos(X,4,20)
# sac.GA_Algorithm(5,12)

from code_1 import Sac_a_dos
# import pandas as pd

# dataset = pd.read_csv('C:\\Users\\sofia\\OneDrive\\Bureau\\ProjetMetaH\\Projet\\sac_a_dos_dataset.csv')

# X = dataset.iloc[:,1:].values
# print(X)
# sac = Sac_a_dos(X,4,20)
# # sac.GA_Algorithm(5,12)


# C:\\Users\\sofia\\OneDrive\\Bureau\\ProjetMetaH\\Projet\\sac_a_dos_dataset.csv
# C:\\Users\\sofia\\OneDrive\\Bureau\\ProjetMetaH\\Projet\\instances_01_KP\\large_scale\\knapPI_1_100_1000_1.csv
import pandas as pd
import numpy as np
# Load the dataset
dataset = pd.read_csv('C:\\Users\\sofia\\OneDrive\\Documents\\instances_01_KP\\low-dimensional\\f8_l-d_kp_23_10000.csv')

# Extract the features again
X = dataset.iloc[:-1, :].values
# print(X)
X = [list(map(int, row[0].split())) for row in X]
X = np.array(X)
X = X[:, ::-1]
# print(X)
sac = Sac_a_dos(X,6,10000)
sac.GA_Algorithm(5,20)
# 9767