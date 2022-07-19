import numpy as np
from scipy.spatial.distance import pdist
from sklearn.neighbors import KernelDensity
import sklearn.cluster

def distance(clusters):
    
    return pdist(clusters)

def average(distances):
    
    # fill this in 
    
    return np.average(distances)

X = np.load('SDSS_Great_Wall_data.npy')
kmeans = sklearn.cluster.KMeans().fit(X)
cluster_centers = kmeans.cluster_centers_ #predict()

