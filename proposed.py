import networkx as nx
import numpy as np
import math
import operator
import scipy.stats

# #-----------------------proposed measure------------------------#
def mutual_reinforce(dataset: "file name", damp = 0.9, iteration = 500):

    G = nx.read_adjlist(dataset)

    #remove isolated nodes
    lst = []
    for node in G.nodes():
        if G.degree(node) == 2 and len(G[node]) == 1:
            lst.append(node)
    for n in lst:
        G.remove_node(n)

    # Initialize all non-zero elements in C to 1
    C = nx.to_numpy_matrix(G, dtype = int)

    # Size of the matrix
    size = int(math.sqrt(np.size(C)))

    # remove loops
    for i in range(size):
        C[i, i] = 0

    # Initialize R to 1
    R = np.full((size, 1), 1)
    #R = np.random.rand(size, 1)

    # Generate the column vector (1 1 1 ... 1)
    one = np.full((size, 1), 1)

    # Default probability (0.15, 0.15, ..., 0.15)
    beta = np.full((size, 1), (1 - damp))

    # Iterate till converge
    for _ in range(iteration):
        # print("R: ")
        # print(R)
        # print()
        # print("C before : ")
        # print(C)

        #C transpose
        C_t = np.transpose(C)

        # print()
        # print("C_t before: ")
        # print(C_t)

        #D'
        D_prime = np.diag(np.squeeze(np.asarray(R)))

        # print()
        # print("D prime: ")
        # print(D_prime)

        #D inverse
        M = np.matmul(C_t, one)
        D = np.diag(np.squeeze(np.asarray(M)))

        # print()
        # print("D: ")
        # print(D)

        D_inv = np.linalg.inv(D)

        # print()
        # print("D inverse: ")
        # print(D_inv)

        # C = D_prime x D_inv x C_t
        inter = np.matmul(D_prime, D_inv)
        C = np.matmul(inter, C_t)

        # print()
        # print("C after: ")
        # print(C)

        # Compute the updated version of C transpose
        C_t = np.transpose(C)

        # print()
        # print("C_t after: ")
        # print(C_t)

        # R = damp * (C_t x one) + beta
        M = np.matmul(C_t, one)

        # print()
        # print("M: ")
        # print(M)
        
        R = damp * M + beta
 
        # print()
        # print("R[377, 0]: ")
        # print(R[377, 0], sep = ",")
        # print("----------------------")

    #collect results
    result = {}
    for i, node in enumerate(G.nodes()):
        result[node] = R[i, 0]
    
    return result

#------------------------------main------------------------------#
if __name__ == "__main__":
    name = "email_network.txt"
    result1 = mutual_reinforce(name, iteration = 500)
    # result2 = mutual_reinforce(name, iteration = 11000)
    # #network = nx.read_adjlist(name)
    # l1 = []
    # l2 = []
    sorted_result1 = sorted(result1.items(), key=lambda kv: kv[1], reverse = True)
    # sorted_result2 = sorted(result2.items(), key=lambda kv: kv[1], reverse = True)

    # for item in sorted_result1:
    #     l1.append(item[0])
    # for item in sorted_result2:
    #     l2.append(item[0])
    
    # for i in range(100):
    #     print(l1[i], l2[i])

    #print(scipy.stats.spearmanr(l1, l2))

    # Construct the network for PageRank
    #network = nx.read_adjlist(name)

    # Get the result from the proposed measure
    #result = mutual_reinforce(name)

    # Sort the result from the proposed measure based on the ranking
    # sorted_result format: [(node1, ranking1), (node2, ranking2)...]
    # sorted_result = sorted(result.items(), key=lambda kv: kv[1], reverse = True)

    # # Print the top ten
    for i in range(10):
        print(sorted_result1[i])

    #print("------------------------------------------------------------------------------")

    # Same for the PageRank
    # pg = nx.pagerank(network, alpha=0.85)
    # sorted_result2 = sorted(pg.items(), key=lambda kv: kv[1], reverse = True)

    # for i in range(10):
    #     print(sorted_result2[i])

    #----------------backup code-------------------#
    #print(scipy.stats.spearmanr(l1, l2)
    # for item in sorted_result:
    #    l1.append(item[0])
    # for item in sorted_result2:
    #    l2.append(item[0])