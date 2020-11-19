import sys
import numpy as np
import matplotlib.pyplot as plt

def Factorial(n) :
    if n == 0 :
        return 1
    return n * Factorial(n-1)

def binomial_dist(n, k, p):
    if k > n:
        print ('k can not be greater than n')
        sys.exit(1)

    return Factorial(n)/(Factorial(k) * Factorial(n-k)) * pow(p, k) * pow(1-p, n-k)
    
"""
윷놀이 실험 결과와 값을 비교하기 위한 binomial distribution 식을 구현하시오.
"""

def yutNori(step, prob_head=0.5):
    """
    np.random.binomial() 함수를 이용하여 윷놀이 실험을 구현하고
    matplotlib를 이용하여 윷놀이 실험 결과를 그래프로 나타내시오.
    """
    a = np.random.binomial(4, prob_head, step)

    mo = 0
    do = 0
    gae = 0
    geol = 0
    yut = 0

    mo_truth = binomial_dist(4, 0, 0.5)
    do_truth = binomial_dist(4, 1, 0.5)
    gae_truth = binomial_dist(4, 2, 0.5)
    geol_truth = binomial_dist(4, 3, 0.5)
    yut_truth = binomial_dist(4, 4, 0.5)

    for i in range(0, step):
        if (a[i] == 0):
            mo += 1
        elif (a[i] == 1):
            do += 1
        elif (a[i] == 2):
            gae += 1
        elif (a[i] == 3):
            geol += 1
        elif (a[i] == 4):
            yut += 1

    mo = float(mo)/float(step)
    do = float(do)/float(step)
    gae = float(gae)/float(step)
    geol = float(geol)/float(step)
    yut = float(yut)/float(step)
    
    sum_of_probability = mo + do + gae + geol + yut
    if sum_of_probability != 1:
        print ('Sum of probability is not one')
        sys.exit(1)
    print ('Probability mo: %f, %f' %(mo, mo_truth) + \
           '\nProbability do: %f, %f' %(do, do_truth) + \
           '\nProbability gae: %f, %f' %(gae, gae_truth) + \
           '\nProbability geol: %f, %f' %(geol, geol_truth) + \
           '\nProbability yut: %f, %f' %(yut, yut_truth))

    fig = plt.figure(figsize=(6.5, 2.5))
    
    yut_result = np.array([mo_truth, do_truth, gae_truth, geol_truth, yut_truth])
    yut_name = np.array(['mo', 'do', 'gae', 'geol', 'yut'])
    yut_ex = np.array([mo, do, gae, geol, yut])

    experiment_Graph = fig.add_subplot(1, 2, 1)
    truth_Graph = fig.add_subplot(1, 2, 2)

    experiment_Graph.bar(yut_name, yut_ex, width = 0.7, color = 'b')
    experiment_Graph.set_title('experiment')
    truth_Graph.bar(yut_name, yut_result, width = 0.7, color = 'r')
    truth_Graph.set_title('truth')
    plt.show()

def main():
    if len(sys.argv) != 2:
        print ('usage: ./yut.py step')
        sys.exit(1)

    step = int(sys.argv[1])

    yutNori(step, 0.5)

if __name__ == '__main__':
    main()
# 이항분포: https://math7.tistory.com/23
