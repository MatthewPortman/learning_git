from file_name import *

def test_distance():
    # fill this in
    
    centers = [[0,0], [1,1], [2,2], [3,3]]
    dis = distance(centers)
    assert sum(dis - np.array([1.41421356, 2.82842712, 4.24264069, 1.41421356, 2.82842712, 1.41421356])) < 0.0000001

def test_average():
    # fill this in 
    centers = [[0,0], [1,1], [2,2], [3,3]]
    avg = average(centers)
    assert avg == 1.5

