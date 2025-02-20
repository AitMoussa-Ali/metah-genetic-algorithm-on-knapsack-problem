# from code_1 import Sac_a_dos
# import pandas as pd

# dataset = pd.read_csv('C:\\Users\\sofia\\OneDrive\\Bureau\\ProjetMetaH\\codes\\sac_a_dos_dataset.csv')
# # print(dataset)
# X = dataset.iloc[:,1:].values

# sac = Sac_a_dos(X,4,20)
# sac.GA_Algorithm(5,12)

from code_1 import Sac_a_dos
from code_2 import Sac_a_dos_2
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
dataset = pd.read_csv('C:\\Users\\sofia\\OneDrive\\Bureau\\Projet metah\\instances_01_KP\\large_scale\\knapPI_1_100_1000_1.csv')
#C:\Users\sofia\OneDrive\Bureau\Projet metah\instances_01_KP\large_scale\knapPI_1_100_1000_1.csv
#C:\\Users\\sofia\\OneDrive\\Bureau\\Projet metah\\instances_01_KP\\low-dimensional\\f1_l-d_kp_10_269.csv
# Extract the features again
X = dataset.iloc[:-1, :].values
# print(X)
X = [list(map(int, row[0].split())) for row in X]
X = np.array(X)
X = X[:, ::-1]
# print(X)

sac = Sac_a_dos_2(X,32,995)
# sac.generate_population()
sac.GA_Algorithm(3000,10)

#9147

#best pour 100 = 45 generations score 6051 crossoverRate = 0.8 mutationRate = 0.3 11 individus
#best pour 100 = 58 generations score 6358 crossoverRate = 0.8 mutationRate = 0.3 12 individus
#best pour 100 = 72 generations score 6476 crossoverRate = 0.8 mutationRate = 0.1 14 individus
#best pour 100 = 121 generations score 7554 crossoverRate = 0.8 mutationRate = 0.1 16 individus
#best pour 100 = 162 generations score 7626 crossoverRate = 0.8 mutationRate = 0.1 16 individus
#best pour 100 = 6174 generations score 9147 crossoverRate = 0.8 mutationRate = 0.15 16 individus

#11238
#best pour 200 = 8958 generations score 11238 crossoverRate = 0.8 mutationRate = 0.1 36 individus
