import csv
import secrets

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

def slots_odds():
    odds_list = get_odds('slots.csv')
    # 随机抽取一个赔率作为单次老虎机spin的赔率
    odds = secrets.choice(odds_list)
    return odds

# 模拟小游戏100倍的赔率
def original():
    random_integer = secrets.randbelow(10000) + 1
    formatted_float = random_integer/10000
    formatted_float = float(formatted_float)  # 将字符串转换为浮点数
    if formatted_float <= 0.0096:
        # 赔率 100
        return 100
    else:
        # 赔率 0
        return 0
    
# 模拟百家乐投注庄胜的赔率
def baccarat():
    # 生成一个小于1且大于0的随机浮点数
    random_integer = secrets.randbelow(1000) + 1
    # 确保小数点后3位
    formatted_float = random_integer/1000
    formatted_float = float(formatted_float)  # 将字符串转换为浮点数
    # 中奖率 9.6%，如果中奖
    if formatted_float <= 0.458:
        # 赔率1.95
        return 1.95
    # 如果闲胜
    elif formatted_float <= 0.904:
        # 赔率 0
        return 0
    # 如果平局
    else:
        # 退回投注
        return 1