# 转载--未完成，2048小游戏
import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit', 'Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

letter_code = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_code, actions))


def init():
    # 初始化游戏棋盘
    return 'Game'


def not_game(state):
    # 游戏结束界面
    responses = defaultdict(lambda: state)
    responses['Restart'], responses['Exit'] = 'Init', 'Exit'
    return responses[action]
