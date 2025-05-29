import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from single_player_bet import single_player
from itertools import repeat
def multi_player(relations,odds_list):
    # pool_size = min(len(relations), multiprocessing.cpu_count())  # 限制并发数
    pool_size = 10
    with multiprocessing.Pool(processes=pool_size) as pool:
        results = pool.starmap(single_player, [(relation, odds_list) for relation in relations])
    return results