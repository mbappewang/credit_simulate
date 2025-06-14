import numpy as np
from typing import List, Tuple, Dict
from loguru import logger
import sys



class Baccarat:
    """百家乐游戏模拟器"""
    
    def __init__(self):
        # 初始化游戏时创建牌组
        self.init_eight_decks()
    
    def init_eight_decks(self):
        """创建并初始化8副牌"""
        # 定义扑克牌的花色和点数
        suits = ['♠', '♥', '♣', '♦']
        values = list(range(1, 14))
        # 生成一副牌的所有组合
        single_deck = [(suit, val) for suit in suits for val in values]
        # 8副牌组合在一起
        self.cards = single_deck * 8
        self.total_cards = len(self.cards)
        self.shuffle_cards()
    
    def shuffle_cards(self):
        """洗牌并设置新的切牌点"""
        import random
        random.shuffle(self.cards)
        self.current_pos = 0
        # 切牌点设置在牌组的40%-60%位置
        self.shuffle_point = int(self.total_cards * (random.random() * 0.1 + 0.7))
        logger.info(f"完成洗牌，总计{self.total_cards}张牌，将在发出{self.shuffle_point}张后重新洗牌")
    
    def draw_card(self) -> Tuple[str, int]:
        """发牌函数，到达切牌点时自动洗牌"""
        # 检查是否需要洗牌
        if self.current_pos >= self.shuffle_point:
            logger.info(f"已发出{self.current_pos}张牌，达到切牌点{self.shuffle_point}，开始洗牌")
            self.shuffle_cards()
        
        card = self.cards[self.current_pos]
        self.current_pos += 1
        return card
    
    def get_card_value(self, card: Tuple[str, int]) -> int:
        """计算单张牌的点数，10及以上的牌点数为0"""
        return 0 if card[1] > 9 else card[1]
    
    def calculate_points(self, cards: List[Tuple[str, int]]) -> int:
        """计算一手牌的总点数，取个位数"""
        total = sum(self.get_card_value(card) for card in cards)
        return total % 10
    
    def need_third_card_player(self, player_total: int) -> bool:
        """判断闲家补牌规则：
        - 点数小于等于5时补牌
        - 点数大于5时不补牌
        """
        return player_total <= 5
    
    def need_third_card_banker(self, banker_total: int, player_third_card: Tuple[str, int] = None) -> bool:
        """判断庄家补牌规则：
        1. 庄家点数大于等于7点，不补牌
        2. 庄家点数小于等于2点，必须补牌
        3. 闲家没有补牌且庄家点数小于等于5点，必须补牌
        4. 庄家点数等于3-6点，根据闲家第三张牌决定是否补牌
        """
        # 首先判断明确不需要参考闲家第三张牌的情况
        if banker_total >= 7:
            return False
        if banker_total <= 2:
            return True
        # 闲家没有补牌的情况
        if player_third_card is None:
            return banker_total <= 5  # 当庄家点数小于等于5点时补牌
            
        # 获取闲家第三张牌的点数
        player_value = self.get_card_value(player_third_card)
        
        # 根据庄家点数判断是否补牌
        if banker_total == 3:
            # 庄家3点，闲家补牌不为8时补牌
            return player_value != 8
            
        elif banker_total == 4:
            # 庄家4点，闲家补牌为2-7时补牌
            return player_value not in [0, 1, 8, 9]
            
        elif banker_total == 5:
            # 庄家5点，闲家补牌为4-7时补牌
            return player_value not in [0, 1, 2, 3, 8, 9]
            
        elif banker_total == 6:
            # 庄家6点，闲家补牌为6或7时补牌
            return player_value in [6, 7]
            
        # 其他情况不补牌
        return False

    def play(self) -> Dict:
        """进行一局百家乐游戏"""
        # 发初始牌
        player_cards = [self.draw_card(), self.draw_card()]
        banker_cards = [self.draw_card(), self.draw_card()]
        
        # 先计算最终点数
        player_total = self.calculate_points(player_cards)
        banker_total = self.calculate_points(banker_cards)
        
        # 判定结果
        result = {
            'player_cards': player_cards,
            'banker_cards': banker_cards,
            'player_points': player_total,
            'banker_points': banker_total,
            'player_pair': False,    # 初始化特殊情况为 False
            'banker_pair': False,
            'perfect_pair': False,
        }
        
        # 判断特殊情况（对子判断逻辑）
        player_cards_values = [card[1] for card in player_cards[:2]]
        banker_cards_values = [card[1] for card in banker_cards[:2]]
        
        result['player_pair'] = player_cards_values[0] == player_cards_values[1]
        result['banker_pair'] = banker_cards_values[0] == banker_cards_values[1]
        
        # 完美对子判断
        result['perfect_pair'] = (
            player_cards[0] == banker_cards[0] and 
            player_cards[1] == banker_cards[1]
        )
        
        # 判定胜负
        # 自然赢:
        if len(player_cards) == 2 and len(banker_cards) == 2:
            if player_total >= 8 or banker_total >= 8:
                logger.debug(f"出现天生牌！闲家:{player_total} 庄家:{banker_total}")
                if player_total > banker_total:
                    result['winner'] = 'player'
                elif banker_total > player_total:
                    result['winner'] = 'banker'
                else:
                    result['winner'] = 'tie'
                return result
    
        # 补牌判断
        # 闲家补牌规则
        if self.need_third_card_player(player_total):
            logger.debug("闲家需要补牌")
            player_third_card = self.draw_card()
            player_cards.append(player_third_card)
            player_total = self.calculate_points(player_cards)
            logger.debug(f"闲家补牌后点数: {player_total}")
        else:
            logger.debug("闲家不需要补牌")
            player_third_card = None
            
        # 庄家补牌规则
        if self.need_third_card_banker(banker_total, player_third_card):
            logger.debug("庄家需要补牌")
            banker_third_card = self.draw_card()
            banker_cards.append(banker_third_card)
            banker_total = self.calculate_points(banker_cards)
            logger.debug(f"庄家补牌后点数: {banker_total}")
        else:
            logger.debug("庄家不需要补牌")
        
        # 更新结果中的点数
        result['player_points'] = player_total
        result['banker_points'] = banker_total
        
        # 判定最终胜负
        # 常规判定:
        if player_total > banker_total:
            result['winner'] = 'player'
        elif banker_total > player_total:
            result['winner'] = 'banker'
        else:
            result['winner'] = 'tie'
        
        # 设置幸运6
        result['lucky_six'] = (banker_total == 6 and result['winner'] == 'banker')
        result['lucky_six_three_cards'] = (result['lucky_six'] and len(banker_cards) == 3)
        
        return result

def simulate_game():
    """模拟一局百家乐游戏并打印结果"""
    import random
    random.seed()  # 使用 random.seed() 替代 np.random.seed()
    game = Baccarat()
    result = game.play()
    
    # 打印初始牌
    logger.info("\n初始发牌:")
    logger.info(f"闲家前两张: {[f'{card[0]}{card[1]}' for card in result['player_cards'][:2]]} 点数: {game.calculate_points(result['player_cards'][:2])}")
    logger.info(f"庄家前两张: {[f'{card[0]}{card[1]}' for card in result['banker_cards'][:2]]} 点数: {game.calculate_points(result['banker_cards'][:2])}")
    
    # 解释补牌
    initial_player_points = game.calculate_points(result['player_cards'][:2])
    if len(result['player_cards']) > 2:
        logger.info(f"\n闲家补牌原因: 初始点数为{initial_player_points}点，小于等于5点，需要补牌")
        logger.info(f"闲家补的牌: {result['player_cards'][2][0]}{result['player_cards'][2][1]}")
    else:
        logger.info(f"\n闲家不补牌原因: 初始点数为{initial_player_points}点，大于5点")
    
    initial_banker_points = game.calculate_points(result['banker_cards'][:2])
    if len(result['banker_cards']) > 2:
        player_third = result['player_cards'][2] if len(result['player_cards']) > 2 else None
        logger.info(f"\n庄家补牌原因: 初始点数为{initial_banker_points}点", end='')
        if player_third:
            logger.info(f"，闲家补了第三张牌{player_third[0]}{player_third[1]}，根据补牌规则需要补牌")
        else:
            logger.info("，小于等于5点，需要补牌")
        logger.info(f"庄家补的牌: {result['banker_cards'][2][0]}{result['banker_cards'][2][1]}")
    else:
        logger.info(f"\n庄家不补牌原因: 初始点数为{initial_banker_points}点", end='')
        if initial_banker_points >= 7:
            logger.info("，大于等于7点")
        else:
            logger.info("，根据补牌规则无需补牌")
    
    # 打印最终结果
    logger.info("\n最终结果:")
    logger.info(f"闲家最终牌: {[f'{card[0]}{card[1]}' for card in result['player_cards']]}")
    logger.info(f"庄家最终牌: {[f'{card[0]}{card[1]}' for card in result['banker_cards']]}")
    logger.info(f"闲家最终点数: {result['player_points']}")
    logger.info(f"庄家最终点数: {result['banker_points']}")
    logger.info(f"获胜方: {'闲' if result['winner'] == 'player' else '庄' if result['winner'] == 'banker' else '和'}")
    
    # 打印特殊情况
    if result['player_pair']:
        logger.info("闲对子!")
    if result['banker_pair']:
        logger.info("庄对子!")
    if result['perfect_pair']:
        logger.info("完美对子!")
    if result['lucky_six']:
        logger.info(f"幸运六! ({'三张牌' if result['lucky_six_three_cards'] else '两张牌'})")

def calculate_rtp(simulations: int = 100_000):
    """计算不同投注类型的RTP
    
    Args:
        simulations: 模拟次数，默认10万次
    """
    game = Baccarat()
    
    # 初始化计数器
    wins = {
        'player': 0,    # 闲赢次数
        'banker': 0,    # 庄赢次数
        'tie': 0,       # 和局次数
        'player_pair': 0,  # 闲对子次数
        'banker_pair': 0,  # 庄对子次数
        'perfect_pair': 0  # 完美对子次数
    }
    
    # 开始模拟
    for i in range(simulations):
        # 每1000次才输出一次进度
        if i % 1000 == 0:
            logger.warning(f"已模拟 {i}/{simulations} 次... ({i/simulations*100:.1f}%)")
            
        result = game.play()
        
        # 统计基本玩法
        wins[result['winner']] += 1
        
        # 统计特殊玩法
        if result['player_pair']:
            wins['player_pair'] += 1
        if result['banker_pair']:
            wins['banker_pair'] += 1
        if result['perfect_pair']:
            wins['perfect_pair'] += 1
    
    # 计算RTP
    # 基本玩法赔率：闲1.0, 庄0.95, 和8.0
    # 特殊玩法赔率：对子11.0, 完美对子33.0
    rtps = {
        # 闲家RTP = 赢钱次数*赔率 + 和局次数*退回金额
        '闲': ((wins['player'] * 2.0) + (wins['tie'] * 1.0)) / simulations * 100,
        # 庄家RTP = 赢钱次数*赔率 + 和局次数*退回金额
        '庄': ((wins['banker'] * 1.95) + (wins['tie'] * 1.0)) / simulations * 100,
        # 和局赔率应该是8:1，而不是8，所以总赔率是9（本金1 + 赔率8）
        '和': (wins['tie'] * 9.0) / simulations * 100,
        '闲对子': (wins['player_pair'] * 12.0) / simulations * 100,
        '庄对子': (wins['banker_pair'] * 12.0) / simulations * 100,
    }
    
    logger.warning("=== EVO RTP统计结果 ===")
    logger.warning(f"模拟总次数: {simulations:,}次")  # 使用 warning 级别
    logger.warning("基本玩法(包含和局退回):")
    logger.warning(f"闲: {rtps['闲']:.4f}% (赔率1:1, 赢{wins['player']:,}次, 和局{wins['tie']:,}次)")
    logger.warning(f"庄: {rtps['庄']:.4f}% (赔率1:0.95, 赢{wins['banker']:,}次, 和局{wins['tie']:,}次)")
    logger.warning(f"和: {rtps['和']:.4f}% (赔率8:1, 赢{wins['tie']:,}次)")
    logger.warning("特殊玩法:")
    logger.warning(f"闲对子: {rtps['闲对子']:.4f}% (出现{wins['player_pair']:,}次, 占比{wins['player_pair']/simulations*100:.2f}%)")
    logger.warning(f"庄对子: {rtps['庄对子']:.4f}% (出现{wins['banker_pair']:,}次, 占比{wins['banker_pair']/simulations*100:.2f}%)")
    # logger.warning(f"完美对子: {rtps['完美对子']:.4f}% (出现{wins['perfect_pair']:,}次, 占比{wins['perfect_pair']/simulations*100:.2f}%)")

# 运行示例
if __name__ == "__main__":
# 配置日志系统
    logger.remove()  
    logger.add(
        sink=sys.stderr,
        # level="INFO",  # 只显示警告及以上级别的日志
        level="WARNING",  # 只显示警告及以上级别的日志
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )
    # simulate_game()
    calculate_rtp(100000000)  # 运行RTP计算