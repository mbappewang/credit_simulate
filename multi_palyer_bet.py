import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from single_player_bet import single_player
from itertools import repeat
from logger import logger
import time


def multi_player(date, weekday, relations, odds_list):
    start_time = time.time()
    pool_size = multiprocessing.cpu_count()+2
    logger.info(f"创建进程池，大小: {pool_size}")
    
    with multiprocessing.Pool(processes=pool_size) as pool:
        total_players = len(relations)
        logger.info("============== 任务执行统计 ==============")
        logger.info(f"开始并行处理 {total_players} 个玩家的投注模拟")
        
        results = pool.starmap(single_player, [
            (date, weekday, relation, odds_list) 
            for relation in relations
        ])
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        logger.info(f"{date} {weekday} - 所有玩家模拟完成:")
        logger.info(f"- 总玩家数: {total_players}")
        logger.info(f"- 总耗时: {execution_time:.2f} 秒")
        # logger.info(f"- 平均每个玩家耗时: {(execution_time/total_players):.3f} 秒")
        logger.info(f"- 处理速度: {total_players/execution_time:.1f} 玩家/秒")
        logger.info("============== 任务执行结束 ==============")
    
    return results