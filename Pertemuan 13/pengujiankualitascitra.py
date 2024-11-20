import numpy as np
import cv2

#assuming both has same size
def mse(arrayA, arrayB):
    r, c = arrayA.shape
    sum = 0
    for i in range(r):
        for j in range(c):
            sum = sum + (arrayA[i, j] - arrayB[i%2, j%2])**2

    res = (sum / (r*c))
    return res

def max(array):
    r, c = array.shape
    max = array[0, 0]
    for i in range(r):
        for j in range(c):
            if array[i, j] > max:
                max = array[i, j]

    return max

def mean(array):
    r, c = array.shape
    mean = 0

    for i in range(r):
        for j in range(c):
            mean = mean + array[i, j]

    res = mean / (r*c)
    return res

def variance(array):
    r, c = array.shape
    means = mean(array)
    sum = 0

    for i in range(r):
        for j in range(c):
            sum = (array[i, j] - means)**2

    var = sum / ((r*c) - 1)
    return var

def covariance(arrayA, arrayB):
    r, c = arrayA.shape
    sum = 0

    meanA = mean(arrayA)
    meanB = mean(arrayB)

    for i in range(r):
        for j in range(c):
            sum = (arrayA[i,j] - meanA) * (arrayB[i%2,j%2] - meanB)

    res = sum / ((r*c) - 1)
    return res

def ssim(arrayA, arrayB):
    meanA = mean(arrayA)
    meanB = mean(arrayB)

    covar = covariance(arrayA, arrayB)

    var1 = variance(arrayA)
    var2 = variance(arrayB)

    c1 = (0.01 * (dynamic_range(max(arrayA)) - 1) )**2
    c2 = (0.03 * (dynamic_range(max(arrayA)) - 1) ) **2

    res = (((2 * meanA * meanB) + c1) * ((2 * covar) + c2)) / ( ((meanA**2) + (meanB)**2 + c1) * (var1 + var2 + c2))
    return  res

def normalized_correlation(arrayA, arrayB):
    r, c = arrayA.shape
    sum1 = 0
    sum2 = 0
    sum3 = 0

    for i in  range(r):
        for j in range(c):
            sum1 = sum1 + (arrayA[i,j] * arrayB[i%2,j%2])
            sum2 = sum2 + arrayA[i, j]**2
            sum3 = sum3 + arrayB[i%2, j%2]**2

    res = sum1 / (np.sqrt(sum2) * np.sqrt(sum3))
    return res

def bit_error_rate(arrayA, arrayB):
    r, c = arrayA.shape
    sum = 0

    for i in range(r):
        for j in range(c):
            sum = sum + (arrayA[i, j] ^ arrayB[i%2, j%2])

    res = sum / (r*c)
    return res

def dynamic_range(max_num):
    bit_base = 2 - 1 # 2^1 - 1 = 1
    while bit_base < max_num:
        bit_base = bit_base * 2
    return bit_base


x = cv2.imread("C:\\Users\\mrhitj\\Pictures\\top cinco gatos momentos.jpg", 0)

B = np.array([[6, 1, 3],
     [1, 2, 7],
     [2, 6, 4]])

C = np.array([[7, 4, 1],
      [4, 5, 3],
      [6, 6, 4]])

mse1 = mse(x, B)
mse2 = mse(x, C)

psnr1 = np.log10((dynamic_range(max(x)) - 1) / (mse1**2))
psnr2 = np.log10((dynamic_range(max(x)) - 1) / (mse2**2))

mean1 = mean(x)

var1 = variance(x)
covar1 = covariance(x, B)

ssimxB = ssim(x, B)
NC_xB = normalized_correlation(x, B)
BER = bit_error_rate(x, B)


print(f'B : {mse1, psnr1, }')
print(f'C : {mse2, psnr2}')
print(f'Mean x : {mean1}')
print(f'Var1 x : {var1}')
print(f'Covariance x and B : {covar1}')
print(f'SSIM x and B : {ssimxB}')
print(f'Normalized correlation x and B : {NC_xB}')
print(f'Bit error rate x and B : {BER}')
