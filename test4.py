# coding=utf-8
import json

def func():
    js = "{}"
    a = json.loads(js)
    if a == {}:
        print("yes")

if __name__ == '__main__':
    func()