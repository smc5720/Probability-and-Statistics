import sys
import math
import numpy as np
import matplotlib.pyplot as plt


# m_per의 확률을 가진 m_val 값들 중 n개의 샘플을 k번 복원 추출
def distribution(m_val, m_per, n, k):
    per = [0, 0, 0, 0, 0, 0, 0, 0]
    result = []

    for i in range(0, 8):
        if i != 0:
            per[i] = per[i - 1] + m_per[i]
        else:
            per[i] = m_per[i]

    for i in range(0, k):
        m_sum = 0
        element = []
        for j in range(0, n):
            x = np.random.random()
            index = 0
            while per[index] < x:
                index += 1
                if index >= 8:
                    index = 7
                    break
            element.append(m_val[index])
        for j in element:
            m_sum += j
        result.append(m_sum)

    result.sort()

    return result


# [val, per] 형태의 리스트를 추출한다.
def get_arr(arr):
    index = 0
    t_sum = 0
    result = []

    while t_sum < len(arr):
        n = arr.count(index)
        if n > 0:
            result.append(int(index))
            result.append(float(n/len(arr)))
        index += 1
        t_sum += n

    return result


num_val = [1, 2, 3, 4, 5, 6, 7, 8]
num_per = [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
#num_per = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625]
exp_num = [1, 2, 4, 32]
#exp_num = [1, 8, 16, 32]


fig = plt.figure(figsize=(6, 6))
ylabel = [0.05, 0.10, 0.15, 0.20, 0.25]
#ylabel = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for column in range(4):
    subplot = fig.add_subplot(2, 2, column+1)

    arr_result = distribution(num_val, num_per, exp_num[column], 1000000)
    arr_graph = get_arr(arr_result)

    arr_val = []
    arr_per = []

    for i in range(0, len(arr_graph)):
        if i % 2 == 0:
            arr_val.append(arr_graph[i])
        else:
            arr_per.append(arr_graph[i])
    t_label = "n = " + str(exp_num[column])
    plt.plot()
    plt.scatter(arr_val, arr_per, s = 10, c = "blue", marker = "o", label = t_label)
    if column == 0:
        plt.yticks(ylabel)
    plt.legend()
plt.show()
