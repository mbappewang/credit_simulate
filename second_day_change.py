def change_task(result):
    new_relations = []
    for item in result:
        new_item = {
            'group_id' : item['group_id'],
            'master_id': item['master_id'],
            'sub_id': item.get('sub_id', None),
            'player_id': item['player_id'],
            'up_point': item['up_point'],
            'default_up_point': item['default_up_point'],
            'game_type': item['game_type'],
            'single_bet': item['single_bet'],
            'withdraw_rate': item['withdraw_rate'],
            'uper_identity': item['uper_identity'],
            'bonus': item['bonus'],
            'default_single_bet_amount': item['default_single_bet_amount'],
            'cashback_rate': item['cashback_rate'],
        }
        # 玩家昨日盈亏金额
        change = item['final_balance'] - item['up_point']
        # 如果玩家昨日输了
        if change < 0:
            # 玩家昨天拿到奖励
            if item['bonus'] > 0:
                # 完成流水目标, 前一天的流水目标 = 本金*2 + 奖励 * 20
                if item['wager'] >= item['up_point'] * 2 + item['bonus'] * 20:
                    # 流水打够的 返的就不用减
                    new_bonus = abs(change) * item['cashback_rate']
                    # 充值金额为昨日亏损金额
                    new_up_point = abs(change)
                    # 等比缩单注金额
                    new_single_bet = new_up_point / item['up_point'] * item['single_bet']
                else:
                    # 没有流水打够的 返的就要减
                    new_bonus = (abs(change) - item['bonus']) * item['cashback_rate']
                    if new_bonus < 0:
                        new_bonus = 0
                    # 充值金额为昨日亏损金额
                    new_up_point = abs(change)
                    new_single_bet = new_up_point / item['up_point'] * item['single_bet']
                new_item['bonus'] = new_bonus
                new_item['up_point'] = new_up_point
                new_item['single_bet'] = new_single_bet
            else:
                # 玩家昨天没有拿到奖励
                new_bonus = abs(change) * item['cashback_rate']
                # 充值金额为昨日亏损金额
                new_up_point = abs(change)
                # 等比缩单注金额
                new_single_bet = new_up_point / item['up_point'] * item['single_bet']
                new_item['bonus'] = new_bonus
                new_item['up_point'] = new_up_point
                new_item['single_bet'] = new_single_bet
        else:
            # 如果玩家昨日赢了
            new_item = {
                'group_id' : item['group_id'],
                'master_id': item['master_id'],
                'sub_id': item.get('sub_id', None),
                'player_id': item['player_id'],
                'up_point': item['default_up_point'],  # 如果玩家赢了,恢复默认充值金额
                'default_up_point': item['default_up_point'],
                'game_type': item['game_type'],
                'single_bet': item['default_single_bet_amount'], # 如果玩家赢了,恢复默认单注
                'withdraw_rate': item['withdraw_rate'],
                'uper_identity': item['uper_identity'],
                'bonus': 0,
                'default_single_bet_amount': item['default_single_bet_amount'],
                'cashback_rate': item['cashback_rate'],
            }
        new_relations.append(new_item)
    return new_relations