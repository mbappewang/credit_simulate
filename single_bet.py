import csv
import secrets
import numpy as np

# 获得slots中奖模拟数据,接受程序同目录下的文件名，将首列数据存为oddslist列表
def get_odds(file_name):
    odds_list = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # 确保行不为空
                odds_list.append(float(row[0]))
    return odds_list

# 从get_odds函数获得oddslist,返回老虎机的单次spin赔率

def slots_odds(odds_list):
    # odds_list = get_odds('slots.csv')
    # 随机抽取一个赔率作为单次老虎机spin的赔率
    odds = np.random.choice(odds_list)
    return odds

# 模拟小游戏100倍的赔率
def original():
    rnd = np.random.randint(1, 10001) / 10000.0  # 生成 0.0001 ~ 1.0000 的随机数
    return 100 if rnd <= 0.0096 else 0
    
# 模拟百家乐投注庄胜的赔率
def baccarat():
    # 生成一个 0 到 1 之间的浮点数，保留三位精度
    rnd = np.random.randint(1, 1001) / 1000.0
    
    if rnd <= 0.458:
        return 1.95
    elif rnd <= 0.904:
        return 0
    else:
        return 1