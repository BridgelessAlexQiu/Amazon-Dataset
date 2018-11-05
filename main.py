import construct_network as cn 
import extracter
import networkx as nx

#--------------------------------main()--------------------------------------
if __name__ == "__main__":
    #the list of dicts where each dict consists of an json object
    reviews = []
    reviews = extracter.read_json()
    extracter.write_file(reviews)

    #determine the bipartite relationship and create files
    adj_list = cn.bipartite_relation()
    cn.create_files(adj_list)

    #construct the network
    bipartite_network = nx.read_adjlist("adj_list.txt")
