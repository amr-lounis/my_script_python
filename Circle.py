import numpy as np

side = 20;

a = np.ones([side,side])


def Circle(_array,_x,_y,_r,_d):
    _array = _array.copy()
    for i in range(0,_array.shape[0]):
        for j in range(0,_array.shape[1]):
            eq = (j-_x)**2 + (i-_y)**2 
            if( eq >= (_r)**2 ) & ( eq <= (_r+_d)**2 ):
                _array[i][j]=0
                
    return _array

b = Circle(a,10,10,5,3)

print(b)