# -*-coding:utf-8-*-
import time
import numpy as np
import pprint

alpha_dict = {
    'a': 0.5,
    'b': 0.25,
    'c': 0.125,
    'd': 0.125,
}


# 计算累乘概率
def mul_pos(input_str=''):
    pre_possibility = 1
    input_list = list(input_str)
    for i in input_list:
        pre_possibility = pre_possibility*alpha_dict.get(i)

    return pre_possibility


# 计算码长
def calc_machang(leic_possibility):
    ma_length = np.ceil(-np.log(leic_possibility)/np.log(2))
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
        accu = accu * alpha_dict.get(xulie[i])
    # leiji_pos = (pos_down + pos_up) / 2
    leiji_pos = pos_down

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
            if pre_pos > 0.875:
                jiema_result = jiema_result+'d'
                pre_pos = (pre_pos - accu_dict.get('d')) / alpha_dict.get('d')
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
        如果N小于二进制概率位数，则将二进制小数的第N位进1，然后截取N位
        '''
        pre_result = bin_pos[:pre_length]
        pre_result = bin_jinwei(pre_result)

    else:
        '''
        如果N大于二进制概率位数，则将二进制小数位后面补零至N位，然后截取N位
        '''
        for i in range(pre_length-len(bin_pos)):
            bin_pos.append(0)
            pre_result = bin_pos
    return pre_result


if __name__ == "__main__":
    a = input("请输入序列:")
    accu_dict = accu_pos(alpha_dict)
    pprint.pprint(accu_dict)
    r = calc_xulie_pos(a, accu_pos_dict=accu_dict)
    lei_possibility = mul_pos(a)
    N = calc_machang(leic_possibility=lei_possibility)
    print(N)
    print(r)
    bin_pos = pos_change(r)
    bin_pos = bianma(bin_pos=bin_pos, pre_length=int(N))
    print(bin_pos)
    back_pos = bin2dec(bin_pos)
    print(back_pos)
    result = decode_proceing(back_pos, accu_pos_dict=accu_dict, machang=len(a))
    print(result)
# 测试序列  baacdaba
