import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def randomVal(step, p1, p2, p3, p4):

    arr = []

    p2 = p1+p2
    p3 = p2+p3
    p4 = p3+p4

    for i in range(0, step):
        x = np.random.random()
        if (p1 > x):
            arr.append(1)
        elif (p2 > x):
            arr.append(2)
        elif (p3 > x):
            arr.append(3)
        else:
            arr.append(4)

    return np.array(arr)

def truthMean(per, val):

    mean = 0
    
    for i in range(0, 4):
        mean += per[i] * val[i]
    
    return mean


def truthMean2(arr):

    per = []
    val = []
    check = []

    for i in arr:
        if i in check:
            continue
        else:
            check.append(i)


    for i in check:
        bool_index = (arr == i)
        per.append(float(len(arr[bool_index]))/float(len(arr)))
        val.append(i)
    return truthMean(per, val)

def truthVar(per, val):

    val2 = []
    for i in range(0, 4):
        val2.append(pow(val[i], 2))

    return truthMean(per, val2) - pow(truthMean(per, val), 2)

def truthVar2(arr):

    per = []
    val = []
    check = []

    for i in arr:
        if i in check:
            continue
        else:
            check.append(i)

    for i in check:
        bool_index = (arr == i)
        per.append(float(len(arr[bool_index]))/float(len(arr)))
        val.append(i)
    return truthVar(per, val)

def randXY_func(input_Step):
    X_arr = randomVal(input_Step, 0.2, 0.4, 0.3, 0.1)
    Y_arr = randomVal(input_Step, 0.25, 0.25, 0.25, 0.25) # 1번

    plt.figure()

    cmp = np.full((4, 4), 0)

    for i in range(0, input_Step):
        cmp[X_arr[i]-1, Y_arr[i]-1] += 1

# 2번
    for i in range(1, 5):
        for j in range(1, 5):
            plt.text(i + 0.1, j, "{}/{}" .format(cmp[i-1][j-1], input_Step), fontsize = 7)
    plt.scatter(X_arr, Y_arr, s = 0.1, c = "blue", marker = "o")

# 3번
    print("\n\n3번 문제입니다.\n")
    per_x4 = float(np.sum(cmp[3, :])) / float(input_Step)
    print("Px(4): " + str(per_x4))
    per_y1 = float(np.sum(cmp[:, 0])) / float(input_Step)
    print("Py(1): " + str(per_y1))
    per_x2y3 = float(cmp[1, 2]) / float(input_Step)
    print("Px|y(2|3): " + str(per_x2y3))

# 4번
    print("\n\n4번 문제입니다.\n")
    per_x = np.array([0.2, 0.4, 0.3, 0.1])
    per_y = np.array([0.25, 0.25, 0.25, 0.25])
    val_xy = np.array([1, 2, 3, 4])

    x_exp_mean = np.mean(X_arr)
    x_truth_mean = truthMean2(X_arr)
    y_exp_mean = np.mean(Y_arr)
    y_truth_mean = truthMean2(Y_arr)
    print("E(X) using numpy: " + str(x_exp_mean))
    print("E(X) using my_def: " + str(x_truth_mean))
    print("E(Y) using numpy: " + str(y_exp_mean))
    print("E(Y) using my_def: " + str(y_truth_mean))

# 5번
    print("\n\n5번 문제입니다.\n")
    x_exp_var = np.var(X_arr)
    x_truth_var = truthVar2(X_arr)
    y_exp_var = np.var(Y_arr)
    y_truth_var = truthVar2(Y_arr)
    print("var[X] using numpy: " + str(x_exp_var))
    print("var[X] using my_def: " + str(x_truth_var))
    print("var[Y] using numpy: " + str(y_exp_var))
    print("var[Y] using my_def: " + str(y_truth_var))

# 6번
    print("\n\n6번 문제입니다.\n")
    solution1 = truthMean2(2*X_arr+4)
    solution2 = truthMean2(-1*pow(Y_arr, 2)-1)
    solution3 = truthVar2(3*Y_arr-3)
    print("E[2X+4] = " + str(solution1))
    print("E[-Y^2-1] = " + str(solution2))
    print("var[3Y-3] = " + str(solution3))

#7번
    print("\n\n7번 문제입니다.\n")
    result = 0
    for i in range(1, 5):
        x_index = (X_arr == i)
        for j in range(1, 5):
            P_xy = float(cmp[i-1, j-1])/float(input_Step)
            print("Px,y({}, {}): ".format(i, j) + str(P_xy))

            P_x = float(len(X_arr[x_index]))/float(input_Step)

            y_index = (Y_arr == j)
            P_y = float(len(Y_arr[y_index]))/float(input_Step)
            print("Px({}): ".format(i) + str(P_x))
            print("Py({}): ".format(j) + str(P_y))
            print("Px({}) * Py({}): ".format(i, j) + str(P_x * P_y))
            result += P_x * P_y

            if(j != 4):
                print("")
    print("-----------------------------------------------------------")

    plt.show()

def main():
    if len(sys.argv) != 2:
        print ('usage: ./yut.py step')
        sys.exit(1)

    step = int(sys.argv[1])

    randXY_func(step)

if __name__ == '__main__':
    main()