# common/log_util.py

import logging
import os
from datetime import datetime

# 创建 logger
# 指定日志保存位置
# 设置日志格式

def get_logger():
    # 获取项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 日志目录
    log_dir = os.path.join(BASE_DIR, "logs")

    # 如果 logs 文件夹不存在，就自动创建
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 日志文件名：按日期生成
    log_file = os.path.join(
        log_dir,
        f"test_{datetime.now().strftime('%Y%m%d')}.log"
    )

    logger = logging.getLogger("api_auto_test")
    logger.setLevel(logging.INFO)

    # 防止重复添加 handler，避免日志重复打印
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger