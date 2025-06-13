import numpy as np
from typing import List, Tuple, Dict

class Baccarat:
    def __init__(self):
        # 使用 numpy 创建牌组
        suits = ['♠', '♥', '♣', '♦']
        values = np.arange(1, 14)
        self.cards = np.array([(suit, val) for suit in suits for val in values], 
                            dtype=[('suit', 'U1'), ('value', 'i4')])
        np.random.shuffle(self.cards)
        self.current_pos = 0
    
    def draw_card(self) -> Tuple[str, int]:
        """抽取一张牌"""
        card = self.cards[self.current_pos]
        self.current_pos += 1
        return (card['suit'], card['value'])

    def get_card_value(self, card: Tuple[str, int]) -> int:
        """获取牌面点数"""
        return 0 if card[1] > 9 else card[1]

    def calculate_points(self, cards: List[Tuple[str, int]]) -> int:
        """计算手牌总点数"""
        values = np.array([self.get_card_value(card) for card in cards])
        return np.sum(values) % 10

    def need_third_card_player(self, player_total: int) -> bool:
        """判断闲家是否需要第三张牌"""
        return player_total <= 5

    def need_third_card_banker(self, banker_total: int, player_third_card: Tuple[str, int] = None) -> bool:
        """判断庄家是否需要第三张牌"""
        if banker_total >= 7:
            return False
        if banker_total <= 2:
            return True
        if player_third_card is None:
            return banker_total <= 5
            
        # 使用 numpy 的 where 函数优化规则判断
        player_value = self.get_card_value(player_third_card)
        rules = {
            3: lambda x: x != 8,
            4: lambda x: x not in [0, 1, 8, 9],
            5: lambda x: x not in [0, 1, 2, 3, 8, 9],
            6: lambda x: x in [6, 7]
        }
        return rules.get(banker_total, lambda x: False)(player_value)

    def play(self) -> Dict:
        """进行一局百家乐游戏"""
        # 发初始牌
        player_cards = [self.draw_card(), self.draw_card()]
        banker_cards = [self.draw_card(), self.draw_card()]
        
        player_total = self.calculate_points(player_cards)
        banker_total = self.calculate_points(banker_cards)
        
        player_third_card = None
        # 闲家补牌
        if self.need_third_card_player(player_total):
            player_third_card = self.draw_card()
            player_cards.append(player_third_card)
            player_total = self.calculate_points(player_cards)
        
        # 庄家补牌
        if self.need_third_card_banker(banker_total, player_third_card):
            banker_cards.append(self.draw_card())
            banker_total = self.calculate_points(banker_cards)
        
        # 判定结果
        result = {
            'player_cards': player_cards,
            'banker_cards': banker_cards,
            'player_points': player_total,
            'banker_points': banker_total
        }
        
        # 判定胜负
        result['winner'] = np.where(player_total > banker_total, 'player',
                          np.where(banker_total > player_total, 'banker', 'tie'))
            
        # 判断特殊情况
        cards_array = np.array(player_cards + banker_cards, 
                             dtype=[('suit', 'U1'), ('value', 'i4')])
        result['player_pair'] = cards_array['value'][0] == cards_array['value'][1]
        result['banker_pair'] = cards_array['value'][2] == cards_array['value'][3]
        result['perfect_pair'] = np.array_equal(cards_array[:2], cards_array[2:4])
        result['lucky_six'] = (banker_total == 6 and result['winner'] == 'banker')
        result['lucky_six_three_cards'] = (result['lucky_six'] and len(banker_cards) == 3)
        
        return result

def simulate_game():
    """模拟一局百家乐游戏并打印结果"""
    np.random.seed()  # 确保随机性
    game = Baccarat()
    result = game.play()
    
    print("闲家牌:", [f"{card[0]}{card[1]}" for card in result['player_cards']])
    print("庄家牌:", [f"{card[0]}{card[1]}" for card in result['banker_cards']])
    print(f"闲家点数: {result['player_points']}")
    print(f"庄家点数: {result['banker_points']}")
    print(f"获胜方: {'闲' if result['winner'] == 'player' else '庄' if result['winner'] == 'banker' else '和'}")
    
    if result['player_pair']:
        print("闲对子!")
    if result['banker_pair']:
        print("庄对子!")
    if result['perfect_pair']:
        print("完美对子!")
    if result['lucky_six']:
        print(f"幸运六! ({'三张牌' if result['lucky_six_three_cards'] else '两张牌'})")

# 运行示例
if __name__ == "__main__":
    simulate_game()