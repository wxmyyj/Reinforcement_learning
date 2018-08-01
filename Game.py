"""
Created on 2018年7月29日

@author: YU_QIAN_RAN

@note:石头*剪刀*布
"""
import tkinter as tk
from LM import RL
import time
# statistic of the scores
li = []


def display():
    global lb1, lb2, lb3
    root = tk.Tk()
    root.geometry("550x500+400+100")
    root.title("Game")
    root.resizable(width=False, height=False)
    # 游戏state
    lb1 = tk.Label(root)
    lb1.place(x=240, y=80)
    lb1['text'] = "你要出什么"
    # 游戏action
    lb2 = tk.Label(root)
    lb2.place(x=80, y=180)
    lb2['text'] = "玩家"
    lb3 = tk.Label(root)
    lb3.place(x=420, y=180)
    lb3['text'] = "电脑"
    # 玩家控制器
    btn1 = tk.Button(root, text="石头", command=lambda: do_task("石头"))
    btn1.place(x=50, y=360, height=30, width=100)
    btn2 = tk.Button(root, text="剪刀", command=lambda: do_task("剪刀"))
    btn2.place(x=220, y=360, height=30, width=100)
    btn3 = tk.Button(root, text="布", command=lambda: do_task("布"))
    btn3.place(x=390, y=360, height=30, width=100)
    root.mainloop()


# function of action
def do_task(act):
    lb2['text'] = act
    time.sleep(0.1)
    main()


# function of the game playing
def main():
    player = lb2['text']
    # insert LM here
    RL.get_state(player)
    lb3['text'] = RL.output()
    computer = lb3['text']
    if player == "石头":
        if computer == "石头":
            lb1['text'] = "平局"
            # sign the reward
        elif computer == "剪刀":
            lb1['text'] = "玩家胜"
            # sign the reward
        elif computer == "布":
            lb1['text'] = "电脑胜"
            # sign the reward
    elif player == "剪刀":
        if computer == "石头":
            lb1['text'] = "电脑胜"
            # sign the reward
        elif computer == "剪刀":
            lb1['text'] = "平局"
            # sign the reward
        elif computer == "布":
            lb1['text'] = "玩家胜"
            # sign the reward
    elif player == "布":
        if computer == "石头":
            lb1['text'] = "玩家胜"
            # sign the reward
        elif computer == "剪刀":
            lb1['text'] = "电脑胜"
            # sign the reward
        elif computer == "布":
            lb1['text'] = "平局"
            # sign the reward
    li.append(lb1['text'])


if __name__ == "__main__":
    display()
    with open("sta.txt", 'w') as file:
        for n in li:
            file.write(n + '\n')
