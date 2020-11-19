"""
문제: 확률을 이용하여 PI 값을 근사하는 프로그램.
"""

import numpy as np
"""
TODO 01: matplotlib.pyplot을 plt라는 이름으로 사용할 수 있게 불러오세요.
"""
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9, 2.5))   # plot을 나타낼 Figure 객체 생성

for column in range(3):
    subplot = fig.add_subplot(1, 3, column+1)   # (X, Y, Z): X x Y (행x열)의 Z번째
    subplot.set_xlim([0, 1])    # 해당 plot의 x축의 범위를 제한 [0, 1)
    subplot.set_ylim([0, 1])    # 해당 plot의 y축의 범위를 제한 [0, 1)

    circle = plt.Circle(xy=(0, 0), radius=1, color='black', fill=False)
    subplot.add_artist(circle)
    
    in_x, in_y = [], []
    out_x, out_y = [], []
    steps = 10 * pow(10, column+1)
    matches = 0
    for _ in range(steps):
        """
        TODO 02: numpy 메소드를 이용하여 [0, 1) 범위를 가진 두 실수 x, y를 생성하세요.
        (Hint: numpy의 random 메소드 이용)
        """
        x = np.random.rand(1)
        y = np.random.rand(1)
        
        isin = (x*x + y*y) <= 1
        matches += isin
        if isin:
            in_x.append(x)
            in_y.append(y)
        else:
            out_x.append(x)
            out_y.append(y)

    """
    TODO 03: 원 안에 들어간 점은 파란색으로, 그렇지 못한 점은 빨간색으로 표시하시오.
    (Hint: matplotlib.pyplot.scatter 메소드 이용, 인자 s=0.1로 설정)
    """
    plt.scatter(in_x, in_y, label = 'in_Spot', s = 0.1, c = "blue", marker = "o")
    plt.scatter(out_x, out_y, label = 'out_Spot', s = 0.1, c = "red", marker = "o")
    
    plt.title('steps: ' + str(steps))
    PI = matches / steps * 4

    print('[steps] %d' % steps)
    print('mathces: %d / %d' % (matches, steps))
    print('pi: %.10f' % np.pi)
    print('approximate pi: %.10f' % PI)
    print('difference: %.10f\n' % (abs(np.pi - PI)))

"""
TODO 04: 플롯의 범례(legend)를 추가하시오.
"""
plt.legend(['in', 'out'], bbox_to_anchor=(1,1))
"""
TODO 05: 플롯 창을 띄우세요.
"""
plt.show()
