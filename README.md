# 信用游戏模拟系统

这是一个用于模拟多人信用游戏投注行为的 Python 系统。该系统可以模拟不同游戏类型(老虎机、原始游戏、百家乐)下的玩家投注行为，并生成详细的投注数据报告。

## 功能特点

- 支持多种游戏类型:
  - 老虎机(slots)
  - 原始游戏(original)
  - 百家乐(baccarat)
- 多层级代理结构:
  - 组
  - 总代
  - 子代
  - 玩家
- 多进程并行计算
- 灵活的参数配置
- Excel 格式的结果输出

## 环境要求

- Python 3.10+
- 依赖包:
  - numpy==2.2.6
  - openpyxl==3.1.5
  - pandas==2.2.3
  - python-dateutil==2.9.0.post0
  - pytz==2025.2
  - six==1.17.0

## 安装

1. 克隆项目到本地
2. 创建并激活虚拟环境(推荐)
3. 安装依赖:

```bash
pip install -r requirements.txt
```

## 使用方法

1. 在 `main.py` 中配置模拟参数:

```python
{
    "game_type": "游戏类型",         # 'slots', 'original', 或 'baccarat'
    "group_count": 组数量,           # 每次模拟的组数
    "matser_count": 总代数量,        # 每组中的总代数量
    "sub_count": 子代数量,           # 每组中的子代数量
    "master_player_count": 玩家数量, # 每个总代下的玩家数量
    "sub_player_count": 玩家数量,    # 每个子代下的玩家数量
    "master_up_point": 上分金额,     # 总代玩家的初始金额
    "sub_up_point": 上分金额,        # 子代玩家的初始金额
    "single_bet": 单注金额,          # 每次投注的金额
    "withdraw_rate": 止盈倍数        # 达到初始金额的多少倍时停止
}
```

2. 运行模拟:

```bash
python main.py
```

3. 查看结果:
   程序将在当前目录生成带时间戳的 Excel 文件，包含以下数据:

- group_id: 组 ID
- player_id: 玩家 ID
- uper_identity: 上级身份
- master_id: 总代 ID
- sub_id: 子代 ID
- game_type: 游戏类型
- up_point: 初始金额
- final_balance: 最终余额
- wager: 总投注额
- wager_valid: 有效投注额
- payout: 总派彩额

## 项目结构

- `main.py`: 主程序入口，包含配置参数和执行逻辑
- `group.py`: 负责创建组-总代-子代-玩家关系
- `single_bet.py`: 实现各种游戏类型的单次投注逻辑
- `single_player_bet.py`: 实现单个玩家的投注模拟
- `multi_palyer_bet.py`: 实现多玩家并行投注模拟
- `slots.csv`: 老虎机游戏赔率配置文件
- `requirements.txt`: 项目依赖列表

## 注意事项

1. 确保系统有足够的内存和 CPU 资源处理大规模模拟
2. 建议在使用较大参数前，先用小规模参数测试
3. 结果文件会自动以时间戳命名，避免覆盖之前的结果
4. 可以通过调整 `multi_palyer_bet.py` 中的 `pool_size` 来控制并发数
