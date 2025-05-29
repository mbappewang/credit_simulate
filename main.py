# 导入常用库
import pandas as pd
from datetime import datetime
from multi_palyer_bet import multi_player
from group import create_group_master_sub_player_relation
from single_bet import get_odds

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
    # 从CSV文件中获取老虎机赔率列表
    odds_list = get_odds('slots.csv')
    # 创建组-总代-子代-玩家关系
    relations = create_group_master_sub_player_relation(task_dict)
    # 执行多玩家模拟
    results = multi_player(relations,odds_list)
    # 将结果转换为DataFrame并保存为Excel文件
    df = pd.DataFrame(results)
    # 创建一个 Excel 写入器
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    excel_writer = pd.ExcelWriter(f'{current_time}results.xlsx', engine='openpyxl')
    # 按照指定字段分组
    grouped = df.groupby(['game_type', 'single_bet_amount'])
    # 遍历每个分组，将数据写入不同的sheet
    for (game_type, bet_amount), group_data in grouped:
        # 创建sheet名称
        sheet_name = f'{game_type}_{bet_amount}'
        # 将分组数据写入相应的sheet
        group_data.to_excel(excel_writer, sheet_name=sheet_name, index=False)
    # 保存并关闭Excel文件
    excel_writer.close()