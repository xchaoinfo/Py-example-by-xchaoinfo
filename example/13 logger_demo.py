"""可在运行时，修改日志输出的文件位置"""

import logging

app_db_logger = logging.getLogger()


def set_app_logger(app_logger, log_file, logger_name=None):
    logger_name = logger_name or "app_db_logger"
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
