from code_1 import Sac_a_dos
import pandas as pd

dataset = pd.read_csv('C:\\Users\\sofia\\OneDrive\\Bureau\\ProjetMetaH\\codes\\sac_a_dos_dataset.csv')
# print(dataset)
X = dataset.iloc[:,1:].values

sac = Sac_a_dos(X,4,20)
sac.GA_Algorithm(5,12)