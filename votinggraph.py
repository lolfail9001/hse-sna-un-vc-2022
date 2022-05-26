import numpy as np
import networkx as nx
import scrubber
import os.path
import matplotlib.pyplot as plt

if os.path.exists("votinggraph.csv") == False or\
   os.path.exists("countrylist.csv") == False:
    vote_matrix, country_list = scrubber.scrub_un_docs()

        
    coalition_matrix = np.matmul(vote_matrix,np.transpose(vote_matrix))

    disagreement_matrix = np.zeros(coalition_matrix.shape)

    for i in range(coalition_matrix.shape[0]):
        for j in range(i,coalition_matrix.shape[1]):
            base = np.min([coalition_matrix[i][i],coalition_matrix[j][j]])
            disagreement = (base - coalition_matrix[i][j])/2
            if np.abs(disagreement) < 0.0001 and i != j:
                fully_consistent_countries += 1
                print("Countries {} and {} are fully consistent".format(country_list[i],country_list[j]))
            if i != j:
                disagreement_matrix[i][j] = -np.log(disagreement/base)
                disagreement_matrix[j][i] = -np.log(disagreement/base)
        

    disagreement_graph = nx.from_numpy_matrix(disagreement_matrix)
    nx.write_weighted_edgelist(disagreement_graph,"votinggraph.csv",delimiter=';')
    country_list_file = open("countrylist.csv","w")
    for str in country_list:
        country_list_file.write(str)
        country_list_file.write(';')
    country_list_file.close()

else:
    disagreement_graph = nx.read_weighted_edgelist("votinggraph.csv")
    country_list_file = open("countrylist.csv",'r')
    country_list = country_list_file.read().split(';')
    country_list_file.close()

# Basic statistics from it

most_disagreeable = nx.eigenvector_centrality(disagreement_graph, weight = 'weight')

sorted_centrality_by_contrarianism = {k: v for k, v in sorted(most_disagreeable.items(), key=lambda item: item[1])}

for k in sorted_centrality_by_contrarianism:
    print(country_list[k],":",sorted_centrality_by_contrarianism[k])

