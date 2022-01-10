"""A simple logger implemention based on logging module.
"""

import logging
from logging.handlers import RotatingFileHandler
import sys, os

class Logger():
    def __init__(self, logger_name: str, basic_level: int=logging.DEBUG, stdout_level: int=logging.DEBUG, logfile_dir: str=None, file_level:int=logging.INFO) -> None:

        # create formatter to define the log-printing style
        self.stdout_formatter = logging.Formatter("[%(levelname)s:%(name)s] [%(filename)s:%(lineno)d:%(module)s:%(funcName)s)]\n>> %(message)s")
        self.file_formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s:%(name)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s]\n>> %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # create logger binding some handlers
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(basic_level)

        # create stdout_handler to print information on the terminal
        self.stdout_handler = logging.StreamHandler()
        self.stdout_handler.setLevel(stdout_level)
        self.stdout_handler.setFormatter(self.stdout_formatter)

        self.logger.addHandler(self.stdout_handler)

        # create file_handler to print information in the log file
        if logfile_dir is not None:
            self.file_handler = RotatingFileHandler(logfile_dir, encoding='utf-8', maxBytes=10 * 1024 * 1024, backupCount=100)
            self.file_handler.setLevel(file_level)
            self.file_handler.setFormatter(self.file_formatter)
            self.logger.addHandler(self.file_handler)

    def get_logger(self):
        return self.logger


print(sys.path)
if __name__ == "__main__":
    lg = Logger('test_logger', logfile_dir='./log/test.log').get_logger()
    lg.debug("debug:%s","log test")
    lg.info("info:%s","log test")
    lg.warning("warning:%s","log test")
    lg.error("error:%s","log test")
    lg.critical("critical:%s","log test")

    lg1 = Logger('a_logger', logfile_dir='./log/test.log').get_logger()
    lg1.debug("debug:%s","log test")
    lg1.info("info:%s","log test")
    lg1.warning("warning:%s","log test")
    lg1.error("error:%s","log test")
    lg1.critical("critical:%s","log test")
    