import numpy as np


def generate( num_points = 2000 ):
    num_points = 2000

    vectors_set = []

    for i in xrange(num_points):
        if np.random.random() > 0.5:
            vectors_set.append([np.random.normal(0.0,0.9),
                                np.random.normal(0.0,0.9)])
        else:
            vectors_set.append([np.random.normal(3.0,0.5),
                                np.random.normal(1.0,0.5)])

    return vectors_set
