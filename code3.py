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


# 表转字符串,输出为二进制小数
def list2str1(input_list):
    result_str = '0b'
    length = len(input_list)
    for i in range(length):
        result_str = result_str+str(input_list[i])

    return result_str


# 表转字符串，输出为编码序列
def list2str2(input_list):
    result_str = ''
    length = len(input_list)
    for i in range(length):
        result_str = result_str+str(input_list[i])

    return result_str


# 计算信源熵
def calc_entropy(alpha_dict):
    entropy = 0
    gailv_jihe = list(alpha_dict.values())
    for i in range(len(alpha_dict)):
        entropy = entropy+gailv_jihe[i]*np.log(gailv_jihe[i])
    return entropy


# 计算累计概率
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


# 计算待编码序列的累计概率
def calc_xulie_pro(xulie, accu_pos_dict={}):
    xulie = list(xulie)
    alpha_list = list(alpha_dict.keys())
    pos_down = 0
    pos_up = 0
    accu = 1
    for i in range(len(xulie)):
        accu = accu*alpha_dict.get(xulie[i])
        print(xulie[i])
        pos_up = pos_down + accu*alpha_dict.get(xulie[i]) + pos_up
        pos_down = pos_up-accu*alpha_dict.get(xulie[i])
        # if xulie[i] is not 'a':
        #     pos_down = accu_pos_dict.get(alpha_list(alpha_list.index(xulie[i])-1))+pos_down

    leiji_pos = (pos_down+pos_up)/2

    return leiji_pos


# 计算码长
def calc_machang(leijigailv):
    ma_length = np.ceil(-np.log(leijigailv)/np.log(2))
    return ma_length


# 将累计概率由十进制小数转换为二进制小数
def pos_change(leijigailv):
    bin_pos = dec2bin(leijigailv)
    return bin_pos


# 实现二进制小数进位
def jinwei(pos_list):
    length = len(pos_list)
    for i in range(length-1,-1,-1):
        if pos_list[i] == '0':
            pos_list[i] = '1'
            break
        else:
            pos_list[i] = '0'


# 从小数后截取N位，如果后还有尾数则进位，如果不足则补零
def bianma(bin_pos, pre_length=30):

    if len(bin_pos) == pre_length:
        pre_result = bin_pos
    elif len(bin_pos) >= pre_length:
        '''
        如果N大于二进制概率位数，则将二进制小数的第N位进1，然后截取N位
        '''
        pre_result = bin_pos[:pre_length]
    else:
        '''
        如果N小于二进制概率位数，则将二进制小数位后面补零至N位，然后截取N位
        '''
        for i in range(len(bin_pos, pre_length)):
            bin_pos.append(str(0))
            pre_result = bin_pos
    return pre_result


# # 解码过程
def decode_proceing(rec_pos, machang, accu_pos_dict):
    pre_pos = rec_pos
    alpha_list = list(alpha_dict.keys())
    # print(alpha_list)
    jiema_result = ''
    for i in range(machang):
        for j in range(len(alpha_dict)-1):
            leijigailv = accu_pos_dict.get(alpha_list[j])
            if j == 0:
                if pre_pos <= accu_pos_dict.get(alpha_list[j+1]):
                    jiema_result = jiema_result+alpha_list[j]
                    pre_pos = pre_pos/alpha_dict.get(alpha_list[j])
                    break
            else:
                if accu_pos_dict.get(alpha_list[j]) < pre_pos <= accu_pos_dict.get(alpha_list[j+1]):
                    jiema_result = jiema_result+alpha_list[j+1]
                    pre_pos = pre_pos / alpha_dict.get(alpha_list[j])
                    break

    return jiema_result


if __name__ == "__main__":
    accu_pos_dict = accu_pos(alpha_dict)  # 计算累计概率
    # pprint.pprint(accu_pos_dict)
    a = input("请输入信号序列（长度为4的小写字母：")
    print("procing ...")
    time.sleep(1)
    print("您输入的序列为：{}".format(a))
    time.sleep(1)
    xulie_pos = calc_xulie_pro(a, accu_pos_dict=accu_pos_dict)
    print("您输入序列的概率为：{}".format(xulie_pos))
    time.sleep(1)
    print("正在计算码长......")
    machang = calc_machang(leijigailv=xulie_pos)
    time.sleep(1)
    print("码长N={}".format(machang))
    time.sleep(1)
    bin_pos = dec2bin(xulie_pos)
    print("小数部分转换为二进制为:")
    time.sleep(1)
    bin_pos1 = list2str1(bin_pos)
    print(bin_pos1)
    time.sleep(1)
    print("正在进行算术编码。。。。")
    bianma_result = bianma(bin_pos=bin_pos, pre_length=int(machang))
    bianma_result1 = list2str2(bianma_result)
    time.sleep(1)
    print("编码结果为：")
    time.sleep(1)
    print(bianma_result1)
    time.sleep(1)
    return_pos = bin2dec(bianma_result)
    print("返回概率为:")
    time.sleep(1)
    print(return_pos)
    jiema_str = decode_proceing(return_pos, len(a), accu_pos_dict)
    print("解码中.......")
    time.sleep(1)
    print("解码结果为：{}".format(jiema_str))




