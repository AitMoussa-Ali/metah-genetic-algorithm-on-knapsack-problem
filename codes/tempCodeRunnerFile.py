#for the data with a large scale we remove the last line because it's represent the optimal solution
# df = df[1:, :]  # deleting the first line
# #last parameter is the percentage of mutation (not mutation rate)
# sac = KnapsackProblem1(df, 100, 995, 0.8, 0.01, 110)
# #parameteres are : 1/generations 2/.... 3/elitism rate 
# sac.GA_Algorithm(30,"sd",0.15) #La for large scale and Lo for low scale Exe