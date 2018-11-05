# Author: Zirou Qiu
# Program: Construct the adjacency list of the network
# Date: 11/5/2018

from collections import defaultdict
import networkx as nx
import matplotlib

#--------------------------bipartite_relation()-------------------------
def bipartite_relation(file = "clean.txt", group1 = "user", group2 = "book"):
    """
    # Description: Determine the bipartite relationship from the data file

    # Return: adjacency list (in the graph theory context)
    """
    index = {"user" : 0, "book" : 1, "helpful" : 2, "overall" : 3, "time" : 4}
    g1 = index[group1]
    g2 = index[group2]
    adjacency_list = defaultdict(set)

    with open(file) as f:
        for line in f:
            review = line.split('\t')
            adjacency_list[review[g1]].add(review[g2])

    return adjacency_list

#-----------------------------create_files()----------------------------
def create_files(adj_list : "bipartite relationship"):
    """
    # Description: Based on the bipartite relationship, create the following two files:
        1. adj_list.txt - the adjacency list format for networkx
        2. gephi.csv - the csv format for Gephi
    """
    data_file = open("adj_list.txt", 'w+')
    gephi_file = open("gephi.csv", 'w+')

    for k, s in adj_list.items():
        data_line = gephi_line = k
        for i in s:
            data_line = data_line + ' ' + i
            gephi_line = gephi_line + ',' + i
        data_line += '\n'
        gephi_line += '\n'
        
        data_file.write(data_line)
        gephi_file.write(gephi_line)

    data_file.close()    
    gephi_file.close()

#--------------------------------main()--------------------------------------
if __name__ == "__main__":
    adj_list = bipartite_relation()
    create_files(adj_list)
    #construct the network
    bipartite_network = nx.read_adjlist("adj_list.txt")