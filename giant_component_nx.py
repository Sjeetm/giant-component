# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 00:47:23 2018

@author: Subhajeet
"""
#%%
def giant_component(n):
    """"
    It takes number of nodes(n), and find the threshold probability to fenerate a random graph and to find its giant componenet.
    """
    import networkx as nx
    import numpy as np
    p=1.5/n
    g=nx.fast_gnp_random_graph(n,p)
    t=list(nx.connected_component_subgraphs(g))
    k=[]
    for i in t:
        k.append(nx.number_of_nodes(i))
    i=np.argsort(k)[::-1]
    print('Number of nodes in giant component are :',nx.number_of_nodes(t[i[0]]))
    return nx.draw(t[i[0]],node_size=150)
#%%
def giant_transition(n):
    """
    It takes numberof nodes and shows the transition of giant component.
    """
    import networkx as nx
    import numpy as np
    import matplotlib.pyplot as plt
    p=[0.3/n,1/n,2/n]
    gc=[]
    r=130
    for i in p:
        g=nx.fast_gnp_random_graph(n,i)
        t=list(nx.connected_component_subgraphs(g))
        k=[]
        for i in t:
            k.append(nx.number_of_nodes(i))
        i=np.argsort(k)[::-1]
        gc.append(t[i[0]])
    for i in range(len(gc)):
        r+=1
        plt.subplot(r)
        plt.title("p= %6.3f"%p[i])
        nx.draw(gc[i],node_size=50)