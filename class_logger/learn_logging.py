# @Time:2021/5/20 10:36 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""
logging模块

0、日志名字：日志收集器
1、日志级别(Level)：DEBUG、INFO、WARING、ERROR、CRITICAL(FATAL)
2、输出渠道(Handle)：控制台(StreamHandel)、文件(FileHandler)
3、日志内容(Format)：时间-哪个代码文件-哪行代码-输出内容

logging模块，默认的root日志收集器。 默认输出级别：WARING

定制化日志输出：
1、创建一个日志收集器  logger = logging.getLogger("收集器名字")
2、给日志收集器设置日志级别：logger.setLevel(logging.等级)
3、给日志收集器，创建一个输出渠道：Handler = logging.StreamHandler()
4、给渠道设置一个日志输出内容的格式
5、将设置的格式与渠道关联起来
6、将设置好的渠道添加到日志收集器上
"""

import logging

# logging.info("hello")
# logging.warning("hello,警告级别")

logger = logging.getLogger("log")
# 设置日志输出级别
logger.setLevel(logging.INFO)
# 设置日志输出渠道
Handler1 = logging.StreamHandler()
# 设置渠道输出内容格式
fmt = '%(name)s %(levelname)s  %(pathname)s %(lineno)d %(message)s'
formatter = logging.Formatter(fmt)
# 将设置的格式与渠道关联起来
Handler1.setFormatter(formatter)
# 将设置好的渠道添加到日志收集器上
logger.addHandler(Handler1)

# 添加FileHandler
Handle2 = logging.FileHandler("my_logging.log", encoding="utf-8")
Handle2.setFormatter(formatter)
logger.addHandler(Handle2)

logger.info("第一个日志")

from logging import handlers
