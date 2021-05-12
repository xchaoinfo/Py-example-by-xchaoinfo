"""可在运行时，修改日志输出的文件位置"""

import logging

# 必须给一个名字，否则会返回 logging.root
# 会共用 logging 的根日志 handlers
app_db_logger = logging.getLogger("app_name")


def set_app_logger(app_logger, log_file, logger_name=None):
    logger_name = logger_name or "app_db_logger"
    # 设置日志别名
    app_logger.name = logger_name
    file_handler = logging.FileHandler(
        filename=log_file,
        encoding="utf-8"
    )
    formatter = logging.Formatter(
        fmt='%(levelname)s\t%(process)d\t%(thread)d\t%(asctime)s\t%(message)s',
        datefmt='%m/%d/%Y %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    app_logger.setLevel(logging.INFO)
    # 每次置空所有的 handlers
    app_logger.handlers = []
    app_logger.addHandler(file_handler)


if __name__ == '__main__':
    pass
    """
    其他引用改模块使用方式
    from logger_deom import app_db_logger, set_app_logger
    log_file = "demo.log"
    set_app_logger(app_db_logger, log_file)
    """
