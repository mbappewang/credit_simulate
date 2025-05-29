import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from single_player_bet import single_player
def multi_player(relations):
    # pool_size = min(len(relations), multiprocessing.cpu_count())  # 限制并发数
    pool_size = 10
    with multiprocessing.Pool(processes=pool_size) as pool:
        results = pool.map(single_player, relations)
    return results