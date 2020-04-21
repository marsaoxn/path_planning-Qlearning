# -*- codeing = utf-8 -*-
# @Time : 2020/4/2 16:08
# @Author : liuyi
# @File : test1_v2.py
# @Software : PyCharm
# 和v1的区别是采用的是中文论文的方法
import numpy as np
import random
np.set_printoptions(threshold = 1e6)  # 设置打印数量的阈值
r = np.array([[-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [ 2,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1, 2,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [ 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-0,-1,-1,-1,-1,-0,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1, 2,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-1,-1,-0,-1],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 2,-1, 2],
              [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-0,-1,-1,-1,-1,-0,-1],
#               0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35

              ])

for i in range(36):
    for j in range(36):
        if r[i,j] == 0:
            r[i,j] = 1

# r现在-1是不通，1是可以通过

q = np.zeros([36, 36], dtype=np.float32)

gamma = 0.8

state = random.randint(0,35)  # 初始状态初始化
for step in range(10000):
    next_state_list = []
    for i in range(36):  # 当前state下的所有动作，收集到next_state_list
        if r[state, i] != -1:
            next_state_list.append(i)
    next_state = next_state_list[random.randint(0, len(next_state_list) - 1)]
    qval = r[state, next_state] + gamma * max(q[next_state])  # 注意qval是一个数值
    q[state, next_state] = qval
    state = next_state

print(q)

# 生成路径

state = 0  # 初始状态
print("robot start at {}".format(state))
q1 = q  # q1去循环变成0矩阵

for k in range(35):  # 走遍36个点,这里是rang(36)时会多一步,因为初始状态已经算一步了

    q1[:, state] = 0

    if not q1[state].any():  # 如果此state全是0,就遍历找一个不全是0的state,肯定能找到
        for new_state in range(36):
            if not q1[new_state].any():
                continue
            print("from {} jump to {}".format(state, new_state))
            state = new_state
            break

    q_max = q1[state].max()  # 状态state这一行里的最大值，即回报最大的动作的回报值
    q_max_action = []

    for action in range(36):  # 找回报最大的动作
        if q1[state, action] == q_max:
            q_max_action.append(action)

    next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
    print("the robot goes to " + str(next_state) + '.')
    state = next_state
