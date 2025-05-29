import logging
from logging.handlers import RotatingFileHandler
import sys

# 创建logger对象
logger = logging.getLogger('simulation')
logger.setLevel(logging.INFO)

# 创建文件处理器
file_handler = RotatingFileHandler(
    'simulation.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5,
    encoding='utf-8'
)
file_handler.setLevel(logging.INFO)

# 创建控制台处理器
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加处理器到logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)