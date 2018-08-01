"""
Created on 2018年7月29日

@author: YU_QIAN_RAN

@note:增强学习
"""
import numpy as np
gamma = 0.8
state = 0
action = 0
reward = 0
p = np.array([[0, -5, 10],
              [10, 0, -5],
              [-5, 10, 0]], 'float64')
q = np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])


def get_state(text):
    global state
    if text == "石头":
        state = 0
    elif text == "剪刀":
        state = 1
    elif text == "布":
        state = 2


def q_learning():
    global action
    action = np.argmax(q[state])
    q[state][action] = p[state][action] + gamma*np.max([q[action][0], q[action][1], q[action][2]])
    print(q)
    return action


def output():
    rs = q_learning()
    if rs == 0:
        return "石头"
    elif rs == 1:
        return "剪刀"
    elif rs == 2:
        return "布"


if __name__ == "__main__":
    x = 3
    y = 4
    z = 5
    print(np.max([x, y, z]))
