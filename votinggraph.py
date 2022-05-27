import numpy as np
import networkx as nx
import scrubber
import os.path
import matplotlib.pyplot as plt


def read_or_scrub ():
    if os.path.exists("votinggraph.csv") == False or\
       os.path.exists("countrylist.csv") == False:
        vote_matrix, country_list = scrubber.scrub_un_docs()

        
        coalition_matrix = np.matmul(vote_matrix,np.transpose(vote_matrix))

        disagreement_matrix = np.zeros(coalition_matrix.shape)

        for i in range(coalition_matrix.shape[0]):
            for j in range(i,coalition_matrix.shape[1]):
                base = np.min([coalition_matrix[i][i],coalition_matrix[j][j]])
                disagreement = (base - coalition_matrix[i][j])/2
                if np.abs(disagreement) < 0.00001 and i != j:
                    print("Countries {} and {} are fully consistent".format(country_list[i],country_list[j]))
                    disagreement_matrix[i][j] = 1e+9
                    disagreement_matrix[j][i] = 1e+9
                elif i != j:
                    disagreement_matrix[i][j] = -np.log(disagreement/base)
                    disagreement_matrix[j][i] = -np.log(disagreement/base)
        

        disagreement_graph = nx.from_numpy_matrix(disagreement_matrix)
        nx.write_weighted_edgelist(disagreement_graph,"votinggraph.csv",delimiter=';')
        country_list_file = open("countrylist.csv","w")
        for str in country_list:
            country_list_file.write(str)
            country_list_file.write("\n")
        country_list_file.close()
        return disagreement_graph, country_list
    else:
        disagreement_graph = nx.read_weighted_edgelist("votinggraph.csv",delimiter=';')
        country_list_file = open("countrylist.csv",'r')
        country_list = country_list_file.read().split("\n")
        country_list_file.close()
        print(country_list)
        return disagreement_graph, country_list

# Example of gathering basic statistics from the graph


def sorted_eigenvector_centrality (G):
    graph_ec = nx.eigenvector_centrality(G, weight = 'weight')

    sorted_ec = {k: v for k, v in sorted(graph_ec.items(), key=lambda item: item[1])}
    return sorted_ec

disagreement_graph, country_list = read_or_scrub()
most_contrarian = sorted_eigenvector_centrality(disagreement_graph)

for k in most_contrarian:
    print(country_list[int(k)],":",most_contrarian[k])

