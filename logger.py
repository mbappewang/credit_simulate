from loguru import logger
import sys
import os

# 创建 logs 文件夹(如果不存在)
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# 移除默认的控制台处理器
logger.remove()

# 添加控制台输出
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> - <level>{message}</level>",
    level="INFO"
)

# 添加文件输出
logger.add(
    os.path.join(logs_dir, "simulation_{time}.log"),
    rotation="10 MB",  # 每个文件最大10MB
    retention="1 week",  # 保留1周的日志
    compression="zip",  # 压缩旧日志
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss} - {message}",
    level="INFO"
)

# 导出 logger 对象供其他模块使用
__all__ = ['logger']