from single_bet import slots_odds, baccarat, original

def single_player(relation):
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
    initial_balance = relation['up_point']
    # 单次投注金额
    single_bet_amount = relation['single_bet']
    # 止盈目标余额
    withdraw_balance = relation['withdraw_rate']* initial_balance
    
    # 总投注金额
    wager = 0
    # 总有效流水
    wager_valid = 0
    # 总返奖金额
    payout = 0
    # 玩家当前余额
    balance = initial_balance

    # 模拟投注结果
    match game_type:
        case 'slots':
            # 当用户【余额大于初始余额1%】且【余额小于止盈金额】时，进行模拟
            while balance > initial_balance * 0.01 and balance < withdraw_balance:
                # 余额不足降低投注额
                if balance < single_bet_amount:
                    single_bet_amount = balance * 0.1
                # 用户投注金额累加
                wager += single_bet_amount
                # 用户有效流水增加
                wager_valid += single_bet_amount
                # 用户余额减少
                balance -= single_bet_amount
                # 单次返奖金额
                single_payout = slots_odds() * single_bet_amount
                # 返奖金额累加
                payout += single_payout
                # 用户余额增加
                balance += single_payout
        case 'original':
            # 当用户【余额小于初始余额1%】且【余额小于止盈金额】时，进行模拟
            while balance > initial_balance * 0.01 and balance < withdraw_balance:
                # 余额不足降低投注额
                if balance < single_bet_amount:
                    single_bet_amount = balance * 0.1
                # 用户投注金额累加
                wager += single_bet_amount
                # 用户有效流水增加
                wager_valid += single_bet_amount * 0.2
                # 用户余额减少
                balance -= single_bet_amount
                # 单次返奖金额
                single_payout = slots_odds() * single_bet_amount
                # 返奖金额累加
                payout += single_payout
                # 用户余额增加
                balance += single_payout
        case 'baccarat':
            # 当用户【余额小于初始余额1%】且【余额小于止盈金额】时，进行模拟
            while balance > initial_balance * 0.01 and balance < withdraw_balance:
                # 余额不足降低投注额
                if balance < single_bet_amount:
                    single_bet_amount = balance * 0.1
                # 用户投注金额累加
                wager += single_bet_amount
                # 用户有效流水增加
                wager_valid += single_bet_amount * 0.2
                # 用户余额减少
                balance -= single_bet_amount
                # 单次返奖金额
                single_payout = slots_odds() * single_bet_amount
                # 返奖金额累加
                payout += single_payout
                # 用户余额增加
                balance += single_payout

    result = {
        'group_id': group_id,
        'player_id': player_id,
        'uper_identity': uper_identity,
        'master_id': master_id,
        'sub_id': sub_id,
        'game_type': game_type,
        'up_point': initial_balance,
        'final_balance': balance,
        'wager': wager,
        'wager_valid': wager_valid,
        'payout': payout,
    }
    print(f"玩法 {game_type} 组 {group_id} 总代 {master_id} 子代 {sub_id} 玩家 {player_id}")
    return result  # 返回投注结果