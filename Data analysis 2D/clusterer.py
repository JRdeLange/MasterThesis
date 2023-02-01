import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

def cluster(data, eps, min_samples):
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    return clustering

def clustering_to_list_of_lists(clustering, data):
    labels = clustering.labels_
    n_clusters = labels.max() - labels.min() + 1
    clusters = []
    print(labels, n_clusters)

    for x in range(n_clusters):
        clusters.append([])
    for idx, point in enumerate(data):
        clusters[labels[idx]].append(point)

    return clusters

def plot_points(points_lists):
    # Get number of lists
    num_lists = len(points_lists)
    # Use a different color for each inner list
    for i in range(num_lists):
        x = [point[0] for point in points_lists[i]]
        y = [point[1] for point in points_lists[i]]
        plt.scatter(x, y, c=plt.cm.rainbow(i/num_lists))
    plt.show()
