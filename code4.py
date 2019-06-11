# -*-coding:utf-8-*-
import numpy as np
import pprint
# from bitarray import bitarray
import time

alpha_dict = {
    'a': 0.1,
    'b': 0.4,
    'c': 0.2,
    'd': 0.3,
}


def accu_pos(para_dict):
    accu_pos_dict = {}
    # print(len(alpha_dict))
    for i in range(len(para_dict)):
        pre_pos = 0
        pre_alpha = list(para_dict.keys())[i]
        if i == 0:
            pre_pos = 0
        else:
            for j in range(i):
                pre_pos = list(para_dict.values())[j]+pre_pos
        accu_pos_dict[pre_alpha] = pre_pos

    return accu_pos_dict


# 计算待编码序列的累计概率
def calc_xulie_pro(xulie, accu_pos_dict={}):
    xulie = list(xulie)
    alpha_list = list(alpha_dict.keys())
    pos_down = 0
    pos_up = 0
    accu = 1
    for i in range(len(xulie)):
        print(xulie[i])
        pos_down = pos_down + accu*accu_dict.get(xulie[i])
        pos_up = pos_down + alpha_dict.get(xulie[i])*accu
        print(accu)
        print(pos_up)
        print(pos_down)
        time.sleep(3)
        accu = accu * alpha_dict.get(xulie[i])
    leiji_pos = (pos_down + pos_up) / 2

    return leiji_pos


if __name__ == "__main__":
    a = input("请输入序列:")
    accu_dict = accu_pos(alpha_dict)
    r = calc_xulie_pro(a, accu_pos_dict=accu_dict)
    print(r)






