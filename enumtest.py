# coding=utf-8
from enum import Enum


class BMRunnningStatus:
    RUNNING = 1
    WAITING_MASTER = 2
    FINISHED = 3


class MyObject(object):


    def __init__(self):
        pass

    def get_status(self,runing_status=BMRunnningStatus.FINISHED):
        if runing_status == BMRunnningStatus.RUNNING:
            print("RUNNING")
        elif runing_status == BMRunnningStatus.WAITING_MASTER:
            print("WAITING MASTER")
        elif runing_status == BMRunnningStatus.FINISHED:
            print("FINISHED")
if __name__ == '__main__':
    my = MyObject()
    my.get_status(BMRunnningStatus.WAITING_MASTER)