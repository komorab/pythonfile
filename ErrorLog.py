# 23-5-16 为了写一个错误日志的模板
import time


class ErrorLog:
    """错误日志"""
    def __init__(self):
        self.time = time.time()

    def errorLogOnTimeToDo(self, from_, to):
        return f"time: {self.time}\nfrom: {from_}\nto: {to}"