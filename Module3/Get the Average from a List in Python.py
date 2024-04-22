"""
Get the Average from a List in Python
Python'daki Bir Listeden Ortalamayı Alın

Bu python kodlama alıştırmasında, bir listeden ortalama alabilen bir fonksiyon geliştireceğiz.
"""

import statistics
import numpy
from functools import reduce

def get_avarage(sayilar):
    total = reduce(lambda total, element: total+element, sayilar)
    return total/len(sayilar)

num_list = [1, 2, 3, 4, 5, 6]

print('metod ile', get_avarage(num_list))

print('statistics ile ', statistics.mean(num_list))
print('numpy ile ', numpy.mean(num_list))

print('-------------for loop ile-------------------')
def ortalama_hesapla(nums):
    sum = 0
    elemnet_nums = 0

    for num in nums:
        sum += num
        elemnet_nums += 1

    avarage = sum / elemnet_nums
    return avarage

nums = [1, 2, 3, 4, 5, 6]
print(f"Listenin ortalaması: {ortalama_hesapla(nums)}")

