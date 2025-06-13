from single_bet import slots_odds, baccarat, original
from logger import logger

def single_player(date,weekday,relation,odds_list):
    """
    模拟单个玩家的投注
    :param relation: 玩家关系字典
    :return: 大玩家账户信息
    """
    # 玩家所属组
    group_id = relation['group_id']
    # 玩家ID
    player_id = relation['player_id']
    # 玩家上级身份
    uper_identity = relation['uper_identity']
    # 玩家总代
    master_id = relation['master_id']
    # 玩家子代
    sub_id = relation.get('sub_id', None)  # 子代可能不存在
    # 玩家所选玩法
    game_type = relation['game_type']
    # 玩家初始余额
    initial_balance = relation['up_point'] + relation['bonus']
    # 单次投注金额
    default_single_bet_amount = relation['default_single_bet_amount']
    current_single_bet_amount = relation['single_bet']
    single_bet_amount = relation['single_bet']
    # 止盈目标余额
    withdraw_balance = relation['withdraw_rate'] * relation['up_point'] + relation['bonus']
    
    # 总投注金额
    wager = 0
    # 总有效流水
    wager_valid = 0
    # 总返奖金额
    payout = 0
    # 玩家当前余额
    balance = initial_balance
    # 投注次数
    bet_times = 0

    # 模拟投注结果
    match game_type:
        case 'slots':
            # 当用户余额大于0，且（未达到止盈金额或未完成有效流水）时，继续投注
            while balance > 0 and (balance < withdraw_balance or wager < initial_balance):
                # 余额不足降低投注额
                if balance < single_bet_amount:
                    single_bet_amount = balance * 0.1
                # 如果余额小于默认投注额且大于等于单次投注额，则不改变单次投注额
                elif balance < current_single_bet_amount and balance >= single_bet_amount:
                    pass
                # 否则，使用默认单次投注额
                else:    
                    single_bet_amount = current_single_bet_amount
                if balance <= initial_balance * 0.01:
                    wager += balance
                    balance = 0
                    break  # 如果余额小于初始余额的1%，则退出循环
                # 用户投注金额累加
                wager += single_bet_amount
                # 用户有效流水增加
                wager_valid += single_bet_amount
                # 用户余额减少
                balance -= single_bet_amount
                # 单次返奖金额
                single_payout = slots_odds(odds_list) * single_bet_amount
                # 返奖金额累加
                payout += single_payout
                # 用户余额增加
                balance += single_payout
        case 'original':
            # 当用户余额大于0，且（未达到止盈金额或未完成有效流水）时，继续投注
            while balance > 0 and (balance < withdraw_balance or wager < initial_balance):
                # 余额不足降低投注额
                if balance < single_bet_amount:
                    single_bet_amount = balance * 0.1
                # 如果余额小于默认投注额且大于等于单次投注额，则不改变单次投注额
                elif balance < current_single_bet_amount and balance >= single_bet_amount:
                    pass
                # 否则，使用默认单次投注额
                else:    
                    single_bet_amount = current_single_bet_amount
                if balance <= initial_balance * 0.01:
                    wager += balance
                    balance = 0
                    break  # 如果余额小于初始余额的1%，则退出循环
                # 用户投注金额累加
                wager += single_bet_amount
                # 用户有效流水增加
                wager_valid += single_bet_amount * 0.2
                # 用户余额减少
                balance -= single_bet_amount
                # 单次返奖金额
                single_payout = original() * single_bet_amount
                # 返奖金额累加
                payout += single_payout
                # 用户余额增加
                balance += single_payout
        case 'baccarat':
            # 当用户余额大于0，且（未达到止盈金额或未完成有效流水）且 投注次数小于 250 次 时，继续投注
            while balance > 0 and (balance < withdraw_balance or wager < initial_balance) and bet_times <= 100:
                # 余额不足降低投注额
                if balance < single_bet_amount:
                    single_bet_amount = balance * 0.1
                # 如果余额小于默认投注额且大于等于单次投注额，则不改变单次投注额
                elif balance < current_single_bet_amount and balance >= single_bet_amount:
                    pass
                # 否则，使用默认单次投注额
                else:    
                    single_bet_amount = current_single_bet_amount
                if balance <= initial_balance * 0.01:
                    wager += balance
                    balance = 0
                    break  # 如果余额小于初始余额的1%，则退出循环
                # 用户投注金额累加
                wager += single_bet_amount
                # 用户有效流水增加
                wager_valid += single_bet_amount * 0.2
                # 用户余额减少
                balance -= single_bet_amount
                # 单次返奖金额
                single_payout = baccarat() * single_bet_amount
                # 返奖金额累加
                payout += single_payout
                # 用户余额增加
                balance += single_payout
                # 投注次数增加
                bet_times += 1

    if wager <= relation['up_point'] * 2 + relation['bonus'] * 20:
        balance = balance - relation['bonus']
    if balance < 0:
        balance = 0

    result = {
        'date': date,
        'weekday': weekday,
        'group_id': group_id,
        'player_id': player_id,
        'uper_identity': uper_identity,
        'master_id': master_id,
        'sub_id': sub_id,
        'game_type': game_type,
        'default_single_bet_amount': default_single_bet_amount,
        'single_bet': current_single_bet_amount,
        'up_point': relation['up_point'],
        'final_balance': balance,
        'wager': wager,
        'wager_valid': wager_valid,
        'payout': payout,
        "bonus": relation['bonus'],
        "withdraw_rate": relation['withdraw_rate'],
        "default_up_point": relation['default_up_point'],
        "cashback_rate": relation['cashback_rate'],
    }
    # logger.info(f"日期{date} {weekday}  玩法 {game_type} 组 {group_id} 总代 {master_id} 子代 {sub_id} 玩家 {player_id} ")
    return result  # 返回投注结果