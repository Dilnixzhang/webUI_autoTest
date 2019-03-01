import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):
    #创建logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

    #设置发送目的地--handler,用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    #项目根目录下/logs保存日志
        log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
    #
        log_name = log_path + rq + '.log'
    #定义handler
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
    #在创建一个handler,用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
    #设置日志信息的格式---formatter
    #定义formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
     #为handler添加formatter
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
    #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger


