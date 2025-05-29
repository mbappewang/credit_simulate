# 导入常用库
import pandas as pd
from datetime import datetime
from single_player_bet import single_player
from multi_palyer_bet import multi_player
from group import create_group_master_sub_player_relation

# 模拟任务
if __name__ == '__main__':
    task_dict = [
        {
        # 游戏类型
        "game_type": 'slots',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 1000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 500,
        # 每个玩家的单次投注金额
        "single_bet": 50,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'slots',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 1000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 500,
        # 每个玩家的单次投注金额
        "single_bet": 25,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'slots',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 1000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 500,
        # 每个玩家的单次投注金额
        "single_bet": 10,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'original',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 1000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 500,
        # 每个玩家的单次投注金额
        "single_bet": 50,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'original',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 1000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 500,
        # 每个玩家的单次投注金额
        "single_bet": 25,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'original',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 1000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 500,
        # 每个玩家的单次投注金额
        "single_bet": 10,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'baccarat',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 2000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 1000,
        # 每个玩家的单次投注金额
        "single_bet": 250,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'baccarat',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 2000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 1000,
        # 每个玩家的单次投注金额
        "single_bet": 100,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    {
        # 游戏类型
        "game_type": 'baccarat',
        # 每次模拟组数
        "group_count": 10,
        # 每组中的总代数量
        "matser_count": 5,
        # 每组中的子代数量
        "sub_count": 10,
        # 每组中的总代的玩家数量
        "master_player_count": 100,
        # 每组中的子代的玩家数量
        "sub_player_count": 50,
        # 每个总代的玩家的上分金额
        "master_up_point": 2000,
        # 每个子代的玩家的上分金额
        "sub_up_point": 1000,
        # 每个玩家的单次投注金额
        "single_bet": 50,
        # 每个玩家的止盈倍数
        "withdraw_rate": 3,
    },
    ]
    # 创建组-总代-子代-玩家关系
    relations = create_group_master_sub_player_relation(task_dict[0])
    # 执行多玩家模拟
    results = multi_player(relations)
    # 将结果转换为DataFrame并保存为Excel文件
    df = pd.DataFrame(results)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    df.to_excel(f'{current_time}results.xlsx', index=False)