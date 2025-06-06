# 导入常用库
import pandas as pd
from datetime import datetime, timedelta
from multi_palyer_bet import multi_player
from group import create_group_master_sub_player_relation
from date import generate_dates_with_weekdays
from single_bet import get_odds
import os
from logger import logger
from second_day_change import change_task

# 模拟任务
if __name__ == '__main__':
    
    logger.info(r"""
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                   O\ = /O
                ____/`---'\____
              .'  \\|     |//  `.
             /  \\|||  :  |||//  \\
            /  _||||| -:- |||||-  \\
            |   | \\\  -  /// |   |
            | \_|  ''\---/''  |   |
            \  .-\__  `-`  ___/-. /
          ___`. .'  /--.--\  `. . __
       ."" '<  `.___\_<|>_/___.'  >'"".
      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
      \  \ `-.   \_ __\ /__ _/   .-` /  /
 ======`-.____`-.___\_____/___.-`____.-'======
""")
    
    try:
        ''' 第一步 - 读取task.csv创建任务字典 '''
        try:
            # 读取CSV文件
            task_df = pd.read_csv('task.csv')
            # 将DataFrame转换为字典列表
            task_dict = task_df.to_dict('records')
            logger.info("成功读取任务配置文件")
        except Exception as e:
            logger.error(f"读取任务配置文件失败: {str(e)}")
            raise
        logger.info("=" * 50)
        

        ''' 第二步 - 从CSV文件中获取老虎机赔率列表 '''
        try:
            odds_list = get_odds('slots.csv')
            logger.info("成功读取赔率配置")
        except Exception as e:
            logger.error(f"读取赔率配置失败: {str(e)}")
            raise
        logger.info("=" * 50)


        ''' 第三步 - 创建玩家与代理的映射关系 '''
        try:
            relations = create_group_master_sub_player_relation(task_dict)
            logger.info(f"成功创建{len(relations)}个玩家关系")
        except Exception as e:
            logger.error(f"创建玩家关系失败: {str(e)}")
            raise
        logger.info("=" * 50)


        ''' 第四步 - 生成日期列表 '''
        try:
            dates_list = generate_dates_with_weekdays(7)
            logger.info(f"成功生成{len(dates_list)}天的日期")
        except Exception as e:
            logger.error(f"生成日期列表失败: {str(e)}")
            raise
        logger.info("=" * 50)


        ''' 第五步 - 多玩家投注 '''
        results = []
        try:
            for date_info in dates_list:
                date = date_info['date']
                weekday = date_info['weekday']
                logger.info("=" * 50)
                logger.warning(f"日期: {date}, 星期: {weekday} 的投注模拟开始")
                result = multi_player(date, weekday, relations, odds_list)
                results.extend(result)
                logger.info(f"日期: {date}, 星期: {weekday} 的投注模拟完成")
                new_relations = change_task(result)
        except Exception as e:
            logger.error(f"玩家投注模拟失败: {str(e)}")
            raise
        logger.info("=" * 50)


        ''' 第六步 - 结果处理 '''
        try:
            logger.info("============== 开始处理结果 ==============")
            
            # 定义数值类型列
            numeric_columns = [
                'group_id', 'player_id', 'uper_identity', 'master_id', 'sub_id',
                'single_bet_amount', 'up_point', 'final_balance', 'wager',
                'wager_valid', 'payout', 'bonus', 'withdraw_rate'
            ]
            
            # 创建DataFrame
            df = pd.DataFrame(results)
            
            # 转换数值类型列
            for col in numeric_columns:
                if col in df.columns:
                    # 保存原始数据的副本
                    original_values = df[col].copy()
                    # 尝试转换为数值
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    # 对于无法转换的位置，使用原始值
                    df[col] = df[col].fillna(original_values)
            
            logger.info(f"成功创建DataFrame并转换数据类型, 共{len(df)}条记录")
            
            # 创建csv文件夹
            csv_dir = 'csv'
            if not os.path.exists(csv_dir):
                os.makedirs(csv_dir)
                logger.info(f"创建csv文件夹: {csv_dir}")
            
            # 分组处理
            grouped = df.groupby(['game_type', 'single_bet_amount'])
            group_count = len(grouped)
            logger.info(f"数据分组完成, 共{group_count}个分组")
            
            # 记录每个分组的基本信息并保存CSV
            current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            for (game_type, bet_amount), group_data in grouped:
                file_name = f'{game_type}_{bet_amount}_{current_time}.csv'
                file_path = os.path.join(csv_dir, file_name)
                
                # 保存为CSV时指定数值格式
                group_data.to_csv(
                    file_path,
                    index=False,
                    encoding='utf-8',
                    float_format='%.2f'  # 保留2位小数
                )
                logger.info(f"- 分组 {game_type}_{bet_amount}: {len(group_data)}条记录")
                logger.info(f"  已保存到: {file_path}")
            
            logger.info("============== 结果处理完成 ==============")
            
        except Exception as e:
            logger.error(f"保存结果失败: {str(e)}")
            raise

    except Exception as e:
        logger.error(f"程序执行失败: {str(e)}")
        raise
    else:
        logger.info("程序执行完成")