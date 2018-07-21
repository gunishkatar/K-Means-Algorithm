import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as colormap

# K-Means Algorithm from Scratch

def k_means(data_pts, K_clustering_centers=3, num_iteration=5):

    # Implementing Eucledian Distance Function Inside the K_Means Function
    def distance(x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))
    # New Centers
    New_centers = []

    # Number of Clusters
    k = K_clustering_centers
    # For Final Plotting Of Clusters
    Dict_of_Points = {}
    List_of_Points = []
    for idd in range(k):
        Dict_of_Points[idd] = {
            'points': List_of_Points
        }
    # Genrate Clusters Centers
    clusters = {}

    # K Numbers of Colours will be generated using ColorMaps from Matplotlib
    # Rather than Hardcoding It
    colors = colormap.rainbow(np.linspace(0, 1, k))

    for kx in range(k):
        cluster_id = kx
        points = []
        dim = data_X.shape[1]
        center = 10.0 * (np.random.random((dim,)) * 2 - 1)
        color = colors[kx]
        clusters[cluster_id] = {
            'points': points,
            'center': center,
            'color': color
        }

    for i in range(num_iteration):
        # Allocate points to clusters
        for ix in range(data_X.shape[0]):
            # For each point, get distance with each cluster
            dist = []
            for kx in range(k):
                d = distance(data_X[ix], clusters[kx]['center'])
                dist.append(d)
            # Get cluster id where current point belongs
            c_id = np.argmin(dist)

            clusters[c_id]['points'].append(data_X[ix])

        for kx in range(k):
            pts = np.asarray(clusters[kx]['points'])
            if pts.shape[0] > 0:
                # Compute new cluster center
                new_center = pts.mean(axis=0)
            else:
                new_center = clusters[kx]['center']
            clusters[kx]['points'] = pts
            clusters[kx]['center'] = new_center

        for kx in range(k):
            List_of_Points = clusters[kx]['points']
            Dict_of_Points[kx] = List_of_Points
            clusters[kx]['points'] = []

    for kx in range(k):
        # print clusters[kx]['center']
        New_centers.append(clusters[kx]['center'])

    plt.figure(0)

    for kx in range(k):
        cc = clusters[kx]['center']

        pts = Dict_of_Points[kx]

        try:
            plt.scatter(pts[:, 0], pts[:, 1], color=clusters[kx]['color'])
        except:
            pass

        plt.scatter(cc[0], cc[1], color='black', s=100, marker='*')

    plt.show()

    return New_centers
