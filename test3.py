# coding = utf-8
import traceback

def func():
    try:
        print('test3')
        print("Try start")
        print('test4')
        a = 1/0
        return True
    except Exception as e:
        traceback.print_exc()
        print("exception")
        return False
    finally:
        print("finally")

if __name__ == '__main__':
    print(func())
