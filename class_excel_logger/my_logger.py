# @Time:2021/5/23 4:15 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import logging


class _MyLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        # 设置输出级别、输出渠道、日志格式

        # 继承Logger的初始化类
        super().__init__(name, level)

        # 设置渠道的输出格式
        fmt = '%(name)s %(levelname)s  %(pathname)s %(lineno)d %(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        _Handel1 = logging.StreamHandler()
        _Handel1.setFormatter(formatter)
        self.addHandler(_Handel1)

        # 文件渠道，file不使用默认的None
        if file != None:
            _Handel2 = logging.FileHandler(file, encoding="utf-8")
            _Handel2.setFormatter(formatter)
            self.addHandler(_Handel2)


# 写死路径，引用时候不用再实例化
mylogger = _MyLogger("myLogger", file="MyLogger.log")

if __name__ == '__main__':
    mylogger = _MyLogger("myLogger", file="MyLogger.log")
    mylogger.info("调试封装方法测试")

"""
日志的名字
日志的级别
日志的文件——级别
日志的控制台——级别
日志文件的路径

可配置化

举例：6个测试环境 - 6个数据库 - 1套代码 - 配置文件.conf  .ini
1套封装好的日志功能 - 3个项目

.ini
yaml
"""
