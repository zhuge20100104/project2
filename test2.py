#coding=utf-8


def func(args1,**kwargs):
    print(len(kwargs))
    print('There is xixi!!')
    print('no xixi')
    print('hehe')
    print('xixi')
    print(kwargs)
    print('haha')
    print('hahahaha')
    print('xiddididid')
    kwargs.update(args1)


    # for k,v in kwargs.items():
    #     args1[k] = v
    # print(args1)
if __name__ == '__main__':
    args1={"host":"172.20.25.27:30080"}
    func(args1)


