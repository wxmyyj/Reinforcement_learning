"""
Created on 2018年7月29日

@author: YU_QIAN_RAN

@note:增强学习,5要素，gamma，state，reward，p，q
"""
import numpy as np
gamma = 0.8
state = 0
reward = 0
p = np.array([[0, -1, 1],
              [1, 0, -1],
              [-1, 1, 0]], 'float64')
q = np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]], 'float64')


# 获取状态
def get_state(text):
    global state
    if text == "石头":
        state = 0
    elif text == "剪刀":
        state = 1
    elif text == "布":
        state = 2


# 增强学习中让agent选择最优action
def get_action():
    action_total = q[state]
    the_max = np.max(action_total)
    max_index = []
    for m, n in zip(action_total, range(len(action_total))):
        if m == the_max:
            max_index.append(n)
    choose = int(np.random.random()*len(max_index))
    return max_index[choose]


# Q学习函数
def q_learning():
    global action
    action = get_action()
    q[state][action] = p[state][action] + gamma*np.max([q[action][0], q[action][1], q[action][2]])
    print(q)
    return action


# 输出AI的游戏操作
def output():
    rs = q_learning()
    if rs == 0:
        return "石头"
    elif rs == 1:
        return "剪刀"
    elif rs == 2:
        return "布"


if __name__ == "__main__":
    l1 = [1, 2, 4, 4, 3]
    aa = np.max(l1)
    l2 = []
    for m1, n1 in zip(l1, range(len(l1))):
        if m1 == aa:
            l2.append(n1)
    choose1 = int(np.random.random()*len(l2))
    print(choose1)
    print(l2[choose1])
