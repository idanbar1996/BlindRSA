import math
import random

import sympy


def str_to_num(string):
    byteArray = str_to_bytes(string)
    return int.from_bytes(byteArray, 'big', signed=False)


def num_to_str(num):
    byte_length = math.ceil(num.bit_length() / 8)
    bytes_array = num.to_bytes(byte_length, 'big')
    return bytes_to_str(bytes_array)


def relativly_prime(n):
    k = random.randint(1, n)
    gcd = math.gcd(k, n)
    while gcd != 1:
        k = random.randint(1, n)
        gcd = math.gcd(k, n)
    return k

def str_to_bytes(string):
    return [ord(v) for v in string]

def bytes_to_str(bytes_array):
    char_array = [chr(v) for v in bytes_array]
    return "".join(char_array)

def random_prime():
    sympy.randprime()
#
# def str_to_num2(string):
#     sumVal = 0
#     for v in string:
#         sumVal *= 256
#         sumVal += ord(v)
#     return sumVal
#
#
# def num_to_str2(num):
#     ret = []
#     while num > 0:
#         ret.append(chr(num % 256))
#         num = num // 256
#     return "".join(reversed(ret))
