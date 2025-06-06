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
- 完整日志记录
- 分组CSV格式输出
- 多日期连续模拟
- 动态奖励调整

## 环境要求

- Python 3.10+
- 依赖包:
  - pandas==2.2.3
  - numpy==2.2.6
  - loguru==0.7.3
  - python-dateutil==2.9.0.post0
  - pytz==2025.2

## 安装

1. 克隆项目到本地
2. 创建并激活虚拟环境(推荐)
3. 安装依赖:

```bash
pip install -r requirements.txt
```

## 使用方法

1. 配置任务参数 (task.csv):

```csv
game_type,group_count,matser_count,sub_count,master_player_count,sub_player_count,master_up_point,sub_up_point,single_bet,withdraw_rate,bonus
slots,10,5,10,100,50,1000,500,50,3,0
```

2. 准备老虎机赔率配置 (slots.csv)

3. 运行模拟:

```bash
python main.py
```

4. 查看结果:
程序将在 csv 目录下生成按游戏类型和投注金额分组的 CSV 文件。

## 项目结构

### 核心代码文件

- `main.py`: 主程序入口
- `single_player_bet.py`: 单玩家投注逻辑
- `multi_palyer_bet.py`: 多进程并行处理
- `single_bet.py`: 游戏赔率逻辑
- `group.py`: 代理关系管理
- `date.py`: 日期生成工具
- `logger.py`: 日志系统配置
- `second_day_change.py`: 次日数据调整

### 配置文件

- `task.csv`: 任务配置文件
- `slots.csv`: 老虎机赔率配置
- `requirements.txt`: 项目依赖

### 输出目录

- `csv/`: 模拟结果分组数据
- `logs/`: 运行日志文件

## 注意事项

1. 多进程优化
   - 自动使用所有可用CPU核心
   - 进程池动态分配任务
   - 实时显示处理速度

2. 日志系统
   - 分级记录(INFO/ERROR)
   - 自动文件轮转(10MB)
   - 日志压缩备份
   - 保留期限(1周)

3. 数据处理
   - 按游戏类型和投注额分组
   - UTF-8编码保存
   - 自动创建目录

4. 其他
   - 支持多日期连续模拟
   - 动态调整次日参数
   - 异常处理完整
   - 代码模块化
