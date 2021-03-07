import numpy as np

from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    m = np.array([[3, 3, 3, 5, 3, 2, 2, 3],
                  [3, 3, 3, 4, 3, 2, 1, 3],
                  [3, 2, 3, 3, 3, 2, 2, 3],
                  [2, 5, 4, 2, 2, 1, 2, 3],
                  [2, 1, 4, 5, 3, 3, 2, 2]])
    wei = [0.18, 0.13, 0.17, 0.09, 0.04, 0.13, 0.09, 0.17]

    dh = DecisionHelper(m, wei)
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
