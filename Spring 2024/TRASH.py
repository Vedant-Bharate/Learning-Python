import math


def HW2p1_Task1_UCusername(a, b, n):
    X = [0.1]
    Y = [0.2]

    for i in range(n - 1):
        X.append(b * X[i] + a * Y[i] - (Y[i]) ** 3)
        Y.append(X[i + 1])

    min_val = min(X)
    max_val = max(X)
    number_of_bins = 1 + math.ceil(math.log2(n))
    bin_width = (max_val - min_val) / number_of_bins

    freq_dist = [0] * number_of_bins

    for val in X:
        index = min(math.floor((val - min_val) / bin_width), number_of_bins - 1)
        freq_dist[index] += 1
        
    return freq_dist
