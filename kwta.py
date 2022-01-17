import random
import matplotlib.pyplot as plt
import numpy as np
from saturation_function import *
from activation_function import *

def draw(save_data):
    """ fig 1 """
    # output
    fig1 = plt.figure()
    plt.title("output of kwta")
    s = save_data["s"]
    num = len(s)
    s = np.array(s).T
    for idx, data in enumerate(s):
        x = np.arange(len(data))
        plt.plot(x, data)

    """ fig 2 """
    # identify the winner
    fig2 = plt.figure()
    plt.title("identify winners")
    s = np.array(save_data["s"])[-1]
    
    for idx, val in enumerate(save_data["v"]):
        plt.scatter(val, s[idx])
    
    """ show """
    plt.show()

def main():
    """ param """
    param_n = 100
    param_k = 5
    param_v = [round(random.random(), 3) * 10 for i in range(param_n)]
    param_s = [0.0 for i in range(param_n)]
    # todo - how to choose
    scale_factor = 1

    # parameters of QP problem
    beta = 0.08
    niu = 1
    lamda = 1
    miu = 1

    TOTAL_ITER_TIME = 100

    """ save data """
    save_data = {}
    save_data["v"] = param_v
    save_data["s"] = []

    """ main loop """
    iter_time = 0
    while iter_time < TOTAL_ITER_TIME:
        iter_time += 1

        """ lamda """
        delta_lamda = scale_factor \
                    * activation_function_single(
                        x=sum(param_s) - niu * param_k,
                        r = 1)
        lamda = lamda + delta_lamda

        """ s """
        new_param_s = []
        for i in range(param_n):
            s = (1/niu) \
                * saturation_function(niu*param_v[i] / 2 / beta - lamda)
            new_param_s.append(s)

        param_s = new_param_s

        # save data
        save_data["s"].append(param_s)

        # print(iter_time)
        # print("v:{}".format(param_v))
        # print(lamda)
        # print("s:{}".format(param_s))

    draw(save_data)


if __name__ == "__main__":
    main()
