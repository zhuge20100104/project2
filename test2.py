#coding=utf-8


def func(args1,**kwargs):
    print(len(kwargs))

    kwargs.update(args1)
    print(kwargs)


    # for k,v in kwargs.items():
    #     args1[k] = v
    # print(args1)
if __name__ == '__main__':
    args1={"host":"172.20.25.27:30080"}
    func(args1)


