import numpy as np
import networkx as nx
import scrubber
import model
import os.path

def neglog(c):
    return -np.log((c + 1)/2)

def heavyneglog(c):
    return (- np.log((c + 1)/2)) ** 5

def invfun(c):
    return (1 - c)/(1 + c)

def cov(c):
    return c

def cotan(c):
    return 1/np.tan(np.pi * (c + 1)/ 2)

def read_or_scrub (year_from,year_to,fun = cov):
    cache_string_cov = "cache/covariances_{}_{}.csv".format(year_from,year_to)
    cache_string_list = "cache/countrylist_{}_{}.csv".format(year_from,year_to)
    if os.path.exists(cache_string_cov) == False or\
       os.path.exists(cache_string_list) == False:
        vote_matrix, country_list = scrubber.scrub_un_docs(year_from,year_to)
                
        coalition_matrix = np.matmul(vote_matrix,np.transpose(vote_matrix))

        average_votes = np.sum(vote_matrix,1) / vote_matrix.shape[1]
        covariance_matrix = coalition_matrix - vote_matrix.shape[1] * np.outer(average_votes,average_votes)

        stddevs = np.zeros(covariance_matrix.shape[0])
        for i in range(0,covariance_matrix.shape[0]):
            if (covariance_matrix[i][i] <= 0):
                print(country_list[i], covariance_matrix[i][i], vote_matrix[i])
            stddevs[i] = np.sqrt(covariance_matrix[i][i])
        
        for i in range(0,covariance_matrix.shape[0]):
            covariance_matrix[i][i] = 0
            for j in range(i + 1,covariance_matrix.shape[1]):
                covariance_matrix[i,j] = covariance_matrix[i,j]/(stddevs[i] * stddevs[j])
                covariance_matrix[j,i] = covariance_matrix[j,i]/(stddevs[i] * stddevs[j])
                
        voting_matrix = np.zeros(covariance_matrix.shape)
        for i in range(0,covariance_matrix.shape[0]):
            for j in range(0,covariance_matrix.shape[1]):
                voting_matrix[i,j] = fun(covariance_matrix[i,j])
                
        covariance_graph = nx.from_numpy_matrix(covariance_matrix)
        voting_graph = nx.from_numpy_matrix(voting_matrix)
        nx.write_weighted_edgelist(covariance_graph,cache_string_cov,delimiter=';')
        country_list_file = open(cache_string_list,"w")
        for str in country_list:
            country_list_file.write(str)
            country_list_file.write("\n")
        country_list_file.close()
        return voting_graph, country_list, voting_matrix
    else:
        covariance_graph = nx.read_weighted_edgelist(cache_string_cov,delimiter=';')
        country_list_file = open(cache_string_list,'r')
        country_list = country_list_file.read().split("\n")
        country_list_file.close()
        covariance_matrix = nx.to_numpy_matrix(covariance_graph)
        voting_matrix = np.zeros(covariance_matrix.shape)
        for i in range(0,covariance_matrix.shape[0]):
            for j in range(0,covariance_matrix.shape[1]):
                voting_matrix[i,j] = fun(covariance_matrix[i,j])

        voting_graph = nx.from_numpy_matrix(voting_matrix)
        
        return voting_graph, country_list, voting_matrix

def filter_graph (G, filter_dict, verbose = False) :
    bad_edges = []
    for i in range(len(filter_dict)):
        for j in range(i + 1, len(filter_dict)):
            if filter_dict[i] == filter_dict[j]:
                bad_edges.append((i,j))
                bad_edges.append((j,i))
    if verbose:
        print ("Removing {} edges".format(len(bad_edges)))
    G.remove_edges_from(bad_edges)
    return G


def generate_filtered_record (year_from ,  year_to, blocs):
    cache_string_graph = "cache/filtered_{}_{}_{}.csv".format(year_from,year_to,blocs)
    cache_string_list = "cache/countrylist_{}_{}.csv".format(year_from,year_to)
    if os.path.exists(cache_string_graph) == False or\
       os.path.exists(cache_string_list) == False:
        voting_graph, country_list, voting_matrix = read_or_scrub(year_from,year_to)
        indset_dict = model.optimize_scoring(voting_matrix, blocs)
        filtered_graph = filter_graph(voting_graph, indset_dict)
        nx.write_weighted_edgelist(filtered_graph,cache_string_graph,delimiter=';')
        country_list_file = open(cache_string_list,"w")
        for str in country_list:
            country_list_file.write(str)
            country_list_file.write("\n")
        country_list_file.close()
        return filtered_graph, country_list
    else:
        filtered_graph = nx.read_weighted_edgelist(cache_string_graph,delimiter=';')
        country_list_file = open(cache_string_list,"r")
        country_list = country_list_file.read().split("\n")
        country_list_file.close()
        return filtered_graph, country_list


def spell_community_difference(G, Graw, res, country_list):
    c = nx.algorithms.community.greedy_modularity_communities(G, weight = 'weight', resolution = res)
    c_raw = nx.algorithms.community.greedy_modularity_communities(Graw, weight = 'weight', resolution = res)

    min, max = 0,0
    if len(c_raw) > len(c):
        min = len(c)
        max = len(c_raw)
    else:
        min = len(c_raw)
        max = len(c)
    for j in range(min):
        print("|Community {0:>30}|".format(j + 1))
        print("------------------------------------------------------------------------------------")
        for i in range(len(country_list)):
            bold_str = "*{}*".format(country_list[i])
            if i in c_raw[j] and str(i) in c[j]:
                print("|{0:>40}|{1:>41}|".format(country_list[i],country_list[i]))
            elif i in c_raw[j]:
                print("|                                        |{0:41}|".format(bold_str))
            elif str(i) in c[j]:
                print("|{0:>40}|                                         |".format(bold_str))
    for j in range(min,max):
        print("|Community {0:>30}|".format(j + 1))
        print("------------------------------------------------------------------------------------")
        for i in range(len(country_list)):
            bold_str = "*{}*".format(country_list[i])
            if min == len(c):
                if i in c_raw[j]:
                    print("|                                        |{0:>40}|".format(bold_str))
            else:
                if str(i) in c[j]:
                    print("|{0:>40}|                                         |".format(bold_str))
