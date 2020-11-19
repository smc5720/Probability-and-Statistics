import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def geometric_experiment(head_prob, step):
    # TODO [1]: 확률이 head_prob인 geometric 분포 결과를
    #           시행 횟수를 step만큼 진행하여 변수 random_var_head에 추출하시오.
    random_var_head = np.random.geometric(head_prob, step)
    max_num = np.max(random_var_head)
   
    exp_x = 0
    exp_x2 = 0
    x_bin = []
    y_bin = []
    y2_bin = []

    x_axis = []
    x_label = []
    
    for i in range(1, max_num+1):
        # TODO [2]: head가 나올 때까지의 횟수가 각각 얼마나 나왔는지 x_bin에 기록하시오.
        #           예) 1회만에 head가 나온 횟수: 3
        #               2회만에 head가 나온 횟수: 12
        #               ...
        bool_idx = (random_var_head == i)
        x_bin.append(len(random_var_head[bool_idx]))
        y_bin.append(x_bin[i-1] / step) # X(i)가 실제로 일어난 확률(experiment)
        y2_bin.append(head_prob * pow(1-head_prob, i-1)) # X(i)가 일어날 수 있는 확률(geometric)

        # TODO [3]: 실험값 x의 기댓값(exp_x)과 x^2의 기댓값(exp_x2)을 누적하시오.
        exp_x += i * y_bin[i-1]
        exp_x2 += pow(i,2) * y_bin[i-1]
        
        x_axis.append(i)
        x_label.append(i)
        
    exp_x2 -= pow(exp_x, 2)

    geo_x = 1/head_prob
    geo_x2 = (1-head_prob)/(pow(head_prob, 2))

    # TODO [4]: 실험값과 이론값의 평균과 분산을 출력하시오.
    print('          Experiment   Geometric')
    print('Mean:     %.4f,      %.4f' %(exp_x, geo_x))
    print('Variance: %.4f,      %.4f' %(exp_x2, geo_x2))

    # TODO [5]: 실험값(Experiment)와 이론값(Geometric)을 범례와 함께 bar plot으로 나타내시오.
    #           단, x축의 범위는 1부터 실험값의 최댓값이 되도록 하시오.

    c = np.full((max_num,), 0.15)
    
    fig = plt.figure()
    
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(x_axis - c, y_bin, color = 'b', width = 0.3, label = 'Experiment')
    ax.bar(x_axis + c, y2_bin, color = 'g', width = 0.3, label = 'Geometric')
    ax.set_xlim([0.5, max_num + 0.5])
    ax.set_xticks(x_label)

    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.legend()
    plt.show()

def main():
    if len(sys.argv) != 3:
        print('usage: ./geo.py head_prob step')
        sys.exit(1)

    head_prob = float(sys.argv[1])
    step = int(sys.argv[2])

    geometric_experiment(head_prob=head_prob, step=step)

if __name__ == '__main__':
    main()

# https://m.blog.naver.com/PostView.nhn?blogId=jihyoseok&logNo=221186189902&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F
# https://m.blog.naver.com/PostView.nhn?blogId=yunjh7024&logNo=220826881369&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F
# https://math7.tistory.com/33?category=471451
# 분산 유도식 시험에 나옴
