import numpy as np

class Locate() :
    def __init__(self):
        pass
    
    def do_sum(self, i1, i2, j1, j2, a):
        s = 0
        for i in range(i1, i2):
            for j in range(j1, j2):
                s += a[i][j]
        return s

    def find(self, a) :
        for i in range(0, 161, 20):
            for j in range(0, 161, 20):
                s = self.do_sum(i, i+40, j, j+40, a)
                
                if s > 244800 :
                    return (j+20, i+20)
        return(-1, -1)


    




