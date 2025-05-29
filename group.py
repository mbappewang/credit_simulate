def create_group_master_sub_player_relation(task_list):
    """
    创建组-总代-子代-玩家关系
    :param mission: 任务字典
    :return: 组-总代-子代-玩家关系
    """
    # 初始化关系字典
    relations = []
    relation = {}
    playerid = 0
    for task in task_list:
        for group_id in range(task['group_count']):
            for master_id in range(task['matser_count']):
                for player_id in range(task['master_player_count']):
                    # 创建总代玩家关系
                    relation = {
                        'group_id': group_id+1,
                        'master_id': master_id+1,
                        'sub_id': None,
                        'player_id': f'master_{master_id+1}_player_{playerid+1}',
                        'up_point': task['master_up_point'],
                        "game_type": task['game_type'],
                        'single_bet': task['single_bet'],
                        'withdraw_rate': task['withdraw_rate'],
                        'uper_identity': 'master',
                    }
                    playerid += 1  # 确保player_id从1开始
                    relations.append(relation)
                    relation = {}
                for sub_id in range(task['sub_count']):
                    for player_id in range(task['sub_player_count']):
                        # 创建子代玩家关系
                        relation = {
                            'group_id': group_id+1,
                            'master_id': master_id+1,
                            'sub_id': sub_id+1,
                            'player_id': f'master_{master_id+1}_sub_{sub_id+1}_player_{playerid+1}',
                            'up_point': task['sub_up_point'],
                            "game_type": task['game_type'],
                            'single_bet': task['single_bet'],
                            'withdraw_rate': task['withdraw_rate'],
                            'uper_identity': 'master',
                        }
                        playerid += 1  # 确保player_id从1开始
                        relations.append(relation)
                        relation = {}
    return relations