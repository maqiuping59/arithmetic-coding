# -*-coding:utf-8-*-
import time
import numpy as np
import pprint

alpha_dict = {
    'a': 0.0575,
    'b': 0.0128,
    'c': 0.0263,
    'd': 0.0285,
    'e': 0.0913,
    'f': 0.0173,
    'g': 0.0133,
    'h': 0.0313,
    'i': 0.0599,
    'j': 0.0006,
    'k': 0.0084,
    'l': 0.0335,
    'm': 0.0235,
    'n': 0.0596,
    'o': 0.0689,
    'p': 0.0192,
    'q': 0.0008,
    'r': 0.0508,
    's': 0.0567,
    't': 0.0706,
    'u': 0.0334,
    'v': 0.0069,
    'w': 0.0119,
    'x': 0.0073,
    'y': 0.0164,
    'z': 0.0007,
    ' ': 0.1928,
}


# 计算码长
def calc_machang(leijigailv):
    ma_length = np.ceil(-np.log(leijigailv)/np.log(2))
    return ma_length


# 十进制小数转换为二进制小数
def dec2bin(x):
    x -= int(x)
    bins = []
    while x:
        x *= 2
        bins.append(1 if x >= 1. else 0)
        x -= int(x)
    return bins


# 二进制小数转换为十进制小数
def bin2dec(b):
    d = 0
    for i, x in enumerate(b):
        d += 2**(-i-1)*x
    return d


# 二进制小数进位
def bin_jinwei(input_bin=[]):
    for i in range(len(input_bin)):
        if input_bin[len(input_bin) - 1 - i] == 0:
            input_bin[len(input_bin) - 1 - i] = 1
            break
        else:
            input_bin[len(input_bin) - i - 1] = 0
    return input_bin


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
def calc_xulie_pos(xulie, accu_pos_dict={}):
    xulie = list(xulie)
    alpha_list = list(alpha_dict.keys())
    pos_down = 0
    pos_up = 0
    accu = 1
    for i in range(len(xulie)):
        pos_down = pos_down + accu*accu_dict.get(xulie[i])
        pos_up = pos_down + alpha_dict.get(xulie[i])*accu
        time.sleep(1)
        accu = accu * alpha_dict.get(xulie[i])
    leiji_pos = (pos_down + pos_up) / 2

    return leiji_pos


# # 解码过程
def decode_proceing(rec_pos, accu_pos_dict, machang=0):
    pre_pos = rec_pos
    alpha_list = list(alpha_dict.keys())
    # print(alpha_list)
    jiema_result = ''
    for i in range(machang):
        for j in range(1, len(alpha_list)):
            leijigailv = accu_pos_dict.get(alpha_list[j])
            if pre_pos > 0.8067:
                jiema_result = jiema_result+' '
                pre_pos = (pre_pos - accu_dict.get(' ')) / alpha_dict.get(' ')
                break
            elif pre_pos < leijigailv:
                jiema_result = jiema_result+alpha_list[j-1]
                pre_pos = (pre_pos-accu_dict.get(alpha_list[j-1])) / alpha_dict.get(alpha_list[j-1])
                break

    return jiema_result


# 将累计概率由十进制小数转换为二进制小数
def pos_change(leijigailv):
    bin_pos = dec2bin(leijigailv)
    return bin_pos


# 从小数后截取N位，如果后还有尾数则进位，如果不足则补零
def bianma(bin_pos, pre_length=30):
    pre_result = []
    if len(bin_pos) == pre_length:
        pre_result = bin_pos
    elif len(bin_pos) >= pre_length:
        '''
        如果N大于二进制概率位数，则将二进制小数的第N位进1，然后截取N位
        '''
        pre_result = bin_pos[:pre_length]
        pre_result = bin_jinwei(pre_result)

    else:
        '''
        如果N小于二进制概率位数，则将二进制小数位后面补零至N位，然后截取N位
        '''
        for i in range(len(bin_pos, pre_length)):
            bin_pos.append(str(0))
            pre_result = bin_pos
    return pre_result


if __name__ == "__main__":
    a = input("请输入序列:")
    accu_dict = accu_pos(alpha_dict)
    pprint.pprint(accu_dict)
    r = calc_xulie_pos(a, accu_pos_dict=accu_dict)
    N = calc_machang(r)
    print(r)
    bin_pos = pos_change(r)
    bin_pos = bianma(bin_pos=bin_pos, pre_length=int(N))
    print(bin_pos)
    back_pos = bin2dec(bin_pos)
    print(back_pos)
    result = decode_proceing(back_pos, accu_pos_dict=accu_dict, machang=len(a))
    print(result)

